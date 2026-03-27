#!/usr/bin/env python3
"""
Molecular Property Prediction Tool - Gradio Version
Run locally: python predict_gradio.py
"""

import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem, Draw
import pickle
import gradio as gr
import warnings
warnings.filterwarnings('ignore')

# Load models
with open('models_rf.pkl', 'rb') as f:
    models = pickle.load(f)

def smiles_to_fingerprint(smiles, radius=2, nBits=2048):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        raise ValueError("Invalid SMILES")
    fp = AllChem.GetMorganFingerprintAsBitVect(mol, radius=radius, nBits=nBits)
    return np.array(fp)

def smiles_to_image(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is None:
        return None
    return Draw.MolToImage(mol, size=(400, 400))

def predict_properties(smiles):
    try:
        fp = smiles_to_fingerprint(smiles).reshape(1, -1)
        mol_image = smiles_to_image(smiles)

        homo = models['HOMO'].predict(fp)[0]
        lumo = models['LUMO'].predict(fp)[0]
        eg = models['Eg'].predict(fp)[0]

        results = f"""### Predictions


- **HOMO:** {homo:.3f} eV

- **LUMO:** {lumo:.3f} eV

- **Optical Bandgap:** {eg:.3f} eV

- **Calculated Bandgap:** {lumo-homo:.3f} eV"""

        return mol_image, results
    except Exception as e:
        return None, f"Error: {str(e)}"

# Create interface
interface = gr.Interface(
    fn=predict_properties,
    inputs=gr.Textbox(label="SMILES", placeholder="c1ccccc1"),
    outputs=[gr.Image(label="Molecule"), gr.Markdown(label="Predictions")],
    examples=[["c1ccccc1"], ["c1ccc2ccccc2c1"]],
    title="Molecular Property Predictor"
)

if __name__ == "__main__":
    interface.launch(share=True)
