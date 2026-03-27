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
 
<img width="5370" height="3565" alt="EDA_visualizations" src="https://github.com/user-attachments/assets/e45d4b04-579e-485e-8714-b2ef887c3a46" />

 
Our dataset contains **1,571 organic acceptor molecules** with measured properties.
 
---
 
### Model Performance

<img width="5365" height="4166" alt="model_performance" src="https://github.com/user-attachments/assets/6b7094d4-bec6-493d-8137-dcd3a179d476" />

 
The model captures the relationship between molecular structure and electronic properties.
 
---

🔬 Step 6: Causal Inference & Counterfactual Molecular Design
 
> **Moving from "What properties does this molecule have?" → "How do we design molecules with the properties we want?"**
 
Standard ML models learn *correlations* from training data. The problem: correlations can be misleading. For example, nitro groups correlate with low HOMO — but is it the nitro group causing it, or is it that nitro-containing molecules *also* happen to have longer conjugation? A correlation model cannot tell the difference, and will fail when applied to new molecular scaffolds.
 
We address this with three new tools:
 
---
 
### 🕸️ Causal Graph
 
A directed graph encoding **chemical domain knowledge** as causal relationships — not patterns learned from data. Each arrow means "this feature causally drives that property."
 
<img width="2968" height="1768" alt="causal_graph" src="https://github.com/user-attachments/assets/37dba119-b54a-47a8-8b2a-652a0171b753" />

 
- 🔵 **Blue nodes** — molecular features (causes)
- 🔴 **Red nodes** — electronic properties (effects)
- 🟠 **Orange node** — confounder (Mol. Weight creates false correlations and must be controlled for)
 
---
 
### 🌡️ Causal Effects Heatmap
 
Using **DoWhy** (Microsoft's causal inference library), we estimate the *true causal effect* of each feature on HOMO, LUMO, and Bandgap — controlling for confounders like molecular weight.
 

 <img width="2562" height="964" alt="causal_effects_heatmap" src="https://github.com/user-attachments/assets/61fc799e-0376-4f8b-8717-4fead82ee8ab" />

- **Red** = feature raises the property
- **Blue** = feature lowers the property
- Numbers show the causal effect in eV after removing confounding
 
---
 
### 🔄 Causal vs Correlation Comparison
 
This chart shows exactly where raw correlations are misleading — where the grey bar (correlation) and red bar (true causal effect) differ significantly, the correlation was confounded.
 
<img width="5370" height="1851" alt="causal_vs_correlation" src="https://github.com/user-attachments/assets/03f00923-4687-4924-9c8d-7cd2baf36099" />

 
---
 
### 🧪 Counterfactual Analysis
 
We ask: *"What would happen to this molecule's properties if we made this structural change?"*
 
The model predicts both the original and the modified molecule, then reports **Δ (delta) = the causal effect of the intervention** — not a correlation.
 
<img width="3364" height="1236" alt="counterfactual_effects" src="https://github.com/user-attachments/assets/3e7bd966-3258-425d-82e2-505f5cf78cce" />

 
**Available interventions:**
- Thiophene → Benzene (removes S atom)
- Benzene → Thiophene (adds S atom, lowers LUMO)
- Add Fluorine — EWG, lowers HOMO & LUMO
- Add Cyano group — strong EWG, widens bandgap
 
---
 
### 🎯 Inverse Design — Target a Specific Bandgap
 
Given a **target bandgap**, the model ranks all structural modifications by how close they get to that target. This transforms the model from a screening tool into a **molecular design assistant**.
 
**Target: 1.5 eV** (useful for solar cell absorbers)
 
!<img width="2165" height="965" alt="inverse_1 5eV" src="https://github.com/user-attachments/assets/be448252-608e-482a-8a20-09cac30b261a" />

 
**Target: 2.2 eV** (useful for blue/green emitters)
 
<img width="2165" height="965" alt="inverse_2 2eV" src="https://github.com/user-attachments/assets/1f810a43-29d2-4eed-a077-2ea3621c732f" />

 
The **green bar** is the best structural modification. The **red dashed line** is the target.
 
---

 
## 🗂️ Project Structure
 
```
📦 molecular-property-prediction
├── 📓 Step_1_Data_Preparation.ipynb            # Merge & clean data
├── 📓 Step_2_Feature_Extraction.ipynb           # SMILES → Numbers
├── 📓 Step_3_Model_Training.ipynb               # Train 5 ML models (LR, SVR, RF, XGB, NN)
├── 📓 Step_4_Evaluation_Visualization.ipynb     # Analyze results with best model (RF)
├── 📓 Step_5_Prediction_Tool_Gradio.ipynb       # Interactive Gradio app
├── 📓 Step_6_Causal_Inference.ipynb             # Causal graph, DoWhy, counterfactuals
├── 📁 Data_files/                               # Input datasets
└── 📁 Each_Step_Output_Download/               # Results, models & visualizations
    ├── models_rf.pkl                            # Random Forest (best)
    ├── models_svr.pkl                           # SVR
    ├── causal_graph.png
    ├── causal_effects_heatmap.png
    ├── causal_vs_correlation.png
    ├── counterfactual_effects.png
    ├── counterfactual_results.csv
    ├── inverse_1.5eV.png
    └── inverse_2.2eV.png
```
 
---
 
## 🎮 How to Use
 
### **Option 1: Google Colab (Easiest — No Setup Required)**
 
1. Click on any notebook above
2. Click "Open in Colab"
3. Run cells in order (just click ▶️)
4. Upload data when prompted
5. Download results
 
---
 
### **Option 2: Local Setup**
 
```bash
# Clone repository
git clone https://github.com/Bsamuel-tech/molecular-property-prediction.git
cd molecular-property-prediction
 
# Install dependencies
pip install rdkit pandas numpy scikit-learn tensorflow xgboost gradio matplotlib seaborn dowhy networkx
 
# Run Gradio app
cd Each_Step_Output_Download
python predict_gradio.py
```
 
---

## 🔬 The Science Behind It
 
### How It Works (Steps 1–5):
 
```
SMILES String → Morgan Fingerprints → ML Model → Predictions
   (Input)        (2048 features)      (RF/XGB)    (3 properties)
```
 
### How Causal Inference Works (Step 6):
 
```
Molecule → Structural Change → Predict Original + Modified → Δ = Causal Effect
                                        ↓
                             Rank by distance to target → Best modification
```
 
---
 
## 📚 Models Tested
 
| Model | Result | Notes |
|-------|--------|-------|
| **Linear Regression** | ❌ R² < 0 | Chemistry is non-linear |
| **SVR (RBF kernel)** | ✅ R² = 0.20–0.36 | Good on small datasets |
| **Random Forest** | ✅ **Best overall** R² = 0.22–0.38 | Wins on HOMO & LUMO |
| **XGBoost** | ✅ **Best on Bandgap** R² = 0.385 | Fast, handles sparse data |
| **Neural Network** | ⚠️ R² negative | Needs 10,000+ samples |
 
**Key lesson:** More complex ≠ better when data is limited (1,571 molecules).
 
---

**NEW:** Beyond prediction - now we can **design molecules** with targeted properties!
 

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
