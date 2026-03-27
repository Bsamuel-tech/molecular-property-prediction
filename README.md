# 🧬 Molecular Property Prediction from SMILES

> Predict HOMO, LUMO, and Optical Bandgap of organic molecules using Machine Learning

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![ML](https://img.shields.io/badge/ML-Scikit--learn-orange.svg)
![Deep Learning](https://img.shields.io/badge/DL-TensorFlow-red.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

---

## 🎯 What Does This Project Do?

Instead of spending days in the lab measuring molecular properties, just **type in a molecule's structure** (SMILES string) and get instant predictions!

**Input:** `c1ccccc1` (Benzene)  or copy any SMILES from excel file and see. 

**Output:** 
- HOMO: -5.54 eV
- LUMO: -3.89 eV  
- Optical Bandgap: 1.46 eV

---

## Try It Yourself!

We built an **interactive web interface** using Gradio - which makes it easier for test 

<img width="1899" height="865" alt="Screenshot 2026-03-23 020031" src="https://github.com/user-attachments/assets/563d5995-82a2-4854-8bfe-0c71c5b5e613" />
<img width="1844" height="878" alt="Screenshot 2026-03-23 020043" src="https://github.com/user-attachments/assets/525eec14-e197-4c08-8691-929d66c52bd3" />

<img width="1881" height="835" alt="Screenshot 2026-03-23 020102" src="https://github.com/user-attachments/assets/890a741d-f457-4089-b242-8f3f4e26403d" />


**Features:**
- 🖼️ See the molecular structure
- 🎯 Get instant predictions
- 📊 Compare with dataset averages
- 📱 Works on any device
- 🔗 Shareable public link

---
## Just a Quick Workflow: 
<img width="2000" height="1469" alt="2_Project-Workflow-Overview" src="https://github.com/user-attachments/assets/f1beaeec-9da9-4d37-b63c-3592244f7fb0" />


## 📊 Project Results

Our best model (Support Vector Regression) achieved:

| Property | R² Score | MAE (eV) | Performance |
|----------|----------|----------|-------------|
| **HOMO** | 0.317 | 0.077 | ⭐⭐⭐ Good |
| **LUMO** | 0.195 | 0.103 | ⭐⭐⭐ Good |
| **Optical Bandgap** | 0.357 | 0.070 | ⭐⭐⭐⭐ Very Good |

**What this means:** Predictions are typically within 0.07-0.10 eV of experimental values!

---

## 📈 Visualizations
 
### Data Distribution
 
 
<img width="5370" height="3565" alt="EDA_visualizations" src="https://github.com/user-attachments/assets/1285315d-f816-4db8-b00d-5eef2721732f" />
 
 
Our dataset contains **1,571 organic acceptor molecules** with measured properties.
 
---
 
### Model Performance
 
 
<img width="5370" height="4166" alt="model_performance" src="https://github.com/user-attachments/assets/fc1a919f-90fa-462e-922b-43bb189a8028" />
 
 
The model captures the relationship between molecular structure and electronic properties.
 
---
 
## 🗂️ Project Structure
 
```
📦 molecular-property-prediction
├── 📓 Step_1_Data_Preparation.ipynb          # Merge & clean data
├── 📓 Step_2_Feature_Extraction.ipynb         # SMILES → Numbers
├── 📓 Step_3_Model_Training.ipynb             # Train ML models
├── 📓 Step_4_Evaluation_Visualization.ipynb   # Analyze results
├── 📓 Step_5_Prediction_Tool_Gradio.ipynb     # Interactive app
├── 📓 Step_6_Causal_Inference.ipynb           # Causal design tool
├── 📁 Data_files/                             # Input datasets
└── 📁 Each_Step_Output_Download/              # Results & models
```
 
---
 
## 🎮 How to Use
 
### **Option 1: Google Colab (Easiest - No Setup Required)**
 
1. Click on any notebook above
2. Click "Open in Colab" 
3. Run cells in order (just click ▶️)
4. Upload data when prompted
5. Download results
 
**Perfect for:** Quick testing, presentations, sharing with team
 
---
 
### **Option 2: Local Setup**
 
```bash
# Clone repository
git clone https://github.com/Bsamuel-tech/molecular-property-prediction.git
cd molecular-property-prediction
 
# Install dependencies
pip install rdkit pandas numpy scikit-learn tensorflow gradio matplotlib seaborn
 
# Run Gradio app
cd Each_Step_Output_Download
python predict_gradio.py
```
 
**Perfect for:** Development, customization, offline use

---

## 🧪 Interactive Gradio Demo
 
Run **Step_5_Prediction_Tool_Gradio.ipynb** to launch the web interface:
 
```python
# The notebook will give you a link like:
Running on public URL: https://abc123.gradio.live
```
 
**Share this link** with anyone - they can use it without installing anything!
 
### What Users Can Do:
- ✅ Enter any SMILES string
- ✅ See the molecular structure
- ✅ Get predictions instantly
- ✅ Try example molecules (Benzene, Naphthalene, etc.)
- ✅ Upload CSV for batch predictions
 
---
 
## 🔬 Step 6: Causal Inference & Molecular Design
 
**NEW:** Beyond prediction - now we can **design molecules** with targeted properties!
 
### What Step 6 Does:
 
Instead of just asking *"What properties does this molecule have?"*, we now answer:
- 🎯 *"How can I design a molecule with HOMO = -5.5 eV?"*
- 🔄 *"What if I replace thiophene with benzene?"*
- 🧪 *"Which modification increases bandgap by 0.2 eV?"*
 
### Key Features:
 
✅ **Causal Graph** - Shows which molecular features *cause* property changes (not just correlations)
 
✅ **Counterfactual Queries** - Test 18 different structural modifications:
- Ring replacements (thiophene ↔ benzene, furan → thiophene)
- Functional groups (add NO₂, CN, CF₃, OH, NH₂)
- Halogen substitutions (F ↔ Cl ↔ Br)
- Conjugation changes (C=C ↔ C-C)
 
✅ **Synthetic Feasibility** - Filters out impractical molecules using QED scoring
 
✅ **Multi-Objective Design** - Optimize HOMO, LUMO, and bandgap simultaneously
 
✅ **Mechanistic Explanations** - Each suggestion includes *why* it works chemically
 
### Example Output:
 
```
Target: HOMO = -5.5 eV, Bandgap = 2.0 eV
 
Top 3 Suggestions:
1. Add NO₂ group → ΔHOMO = -0.15 eV, ΔEg = +0.12 eV (QED: 0.67)
2. Replace benzene with pyridine → ΔHOMO = -0.08 eV, ΔEg = +0.05 eV (QED: 0.71)
3. Add CN group → ΔHOMO = -0.11 eV, ΔEg = +0.09 eV (QED: 0.65)
```
 
### Outputs from Step 6:
- `causal_graph.png` - Visual map of chemical cause-effect relationships
- `causal_vs_correlation.png` - Shows spurious vs real effects
- `counterfactual_effects.png` - Average property changes by modification type
- `counterfactual_results.csv` - Detailed results table
- `inverse_design_*.png` - Suggested modifications for target properties
 
---
 
## 🔬 The Science Behind It
 
### How It Works:
 
```
SMILES String → Morgan Fingerprints → ML Model → Predictions
   (Input)      (2048 features)        (SVR)      (3 properties)
```
 
**1. Input:** Molecule as text (SMILES)
```
Example: c1ccccc1 = Benzene
```
 
**2. Feature Extraction:** Convert to numbers using Morgan Fingerprints
```
Encodes: rings, bonds, atoms, functional groups
Output: 2048 binary features
```
 
**3. Machine Learning:** Support Vector Regression predicts properties
```
Trained on 1,571 molecules
Uses RBF kernel with optimized parameters
```
 
**4. Output:** Electronic properties
```
HOMO, LUMO, Optical Bandgap
```
 
**5. Causal Inference (Step 6):** Design new molecules
```
Causal Graph → Counterfactual Predictions → Inverse Design
```
 
---
 
## 📚 What We Learned
 
### Models Tested:
 
| Model | Description | Result |
|-------|-------------|--------|
| **Linear Regression** | Simple baseline | ❌ Too simple (R² < 0) |
| **Support Vector Regression** | Non-linear with RBF kernel | ✅ **Best** (R² = 0.32-0.36) |
| **Neural Network** | Deep learning | ⚠️ Needs more data |
| **Multi-Output NN** | Predicts all 3 together | ⚠️ Didn't improve |
| **Causal Inference** | DoWhy + Counterfactuals | ✅ **Design tool** |
 
**Winner:** SVR with hyperparameter tuning 🏆
 
---
 
## 💡 Key Insights
 
✅ **What Worked:**
- Morgan Fingerprints capture molecular patterns well
- SVR handles small datasets better than deep learning
- Optical Bandgap is easier to predict than HOMO/LUMO
- Interactive Gradio interface makes it accessible
- **Causal inference separates true effects from correlations**
- **Counterfactual design enables targeted molecular engineering**
 
⚠️ **Limitations:**
- Models trained only on acceptor molecules (not donors)
- R² of 0.3 means 70% of variance unexplained
- Predictions most reliable for molecules similar to training data
- Small dataset (1,571 molecules) limits generalization
 
🚀 **Future Improvements:**
- Collect more training data
- Try Graph Neural Networks
- Add 3D molecular structure features
- Train on donor molecules too
- **Validate counterfactual predictions with DFT calculations**
- **Expand modification library to 50+ transformations**
 
---
 
## 🎓 For Students & Researchers
 
### Perfect Learning Project If You Want To:
- Learn cheminformatics (RDKit)
- Practice machine learning (scikit-learn)
- Build interactive apps (Gradio)
- Work with molecular data
- Create end-to-end ML pipeline
- **Understand causal inference (DoWhy)**
- **Design molecules with targeted properties**
 
### Technologies Used:
- **RDKit** - Chemistry toolkit
- **Scikit-learn** - Machine learning
- **TensorFlow/Keras** - Deep learning
- **Gradio** - Web interface
- **Pandas/NumPy** - Data processing
- **Matplotlib/Seaborn** - Visualization
- **DoWhy** - Causal inference
- **SHAP** - Model explanations
 
---
 
## 👥 Team & Contributions
 
This is an academic project demonstrating ML for molecular property prediction.
 
**Contributions welcome!** Feel free to:
- 🐛 Report bugs
- 💡 Suggest improvements
- 🔧 Submit pull requests
- ⭐ Star if you find it useful
 
## By:
- **Sam**
- **Yiming**
- **Fredric**
 @JUNIA ISEN
---
 
## 📄 License
 
 - Feel free to use for learning and research!
 
---
 
## 🙏 Acknowledgments
 
- Dataset from organic photovoltaic research publications
- RDKit community for chemistry tools
- Gradio team for making ML accessible
 
---
 
## 📞 Questions?
 
Open an issue or check out the notebooks - they have detailed explanations!
 
---
 
**⭐ If this project helped you, give it a star!**
 
---
 
<div align="center">
 
Made with ❤️ for molecular science and machine learning
 
[🔝 Back to Top](#-molecular-property-prediction-from-smiles)
 
</div>
