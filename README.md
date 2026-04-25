<div align="center">

<br/>

```
███╗   ███╗ ██████╗ ██╗     ██████╗ ██████╗ ███████╗██████╗ ██╗  ██╗
████╗ ████║██╔═══██╗██║     ██╔══██╗██╔══██╗██╔════╝██╔══██╗╚██╗██╔╝
██╔████╔██║██║   ██║██║     ██████╔╝██████╔╝█████╗  ██║  ██║ ╚███╔╝
██║╚██╔╝██║██║   ██║██║     ██╔═══╝ ██╔══██╗██╔══╝  ██║  ██║ ██╔██╗
██║ ╚═╝ ██║╚██████╔╝███████╗██║     ██║  ██║███████╗██████╔╝██╔╝ ██╗
╚═╝     ╚═╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝  ╚═╝╚══════╝╚═════╝ ╚═╝  ╚═╝
```

### Molecular Property Prediction from SMILES Strings

_Predicting HOMO · LUMO · Optical Bandgap of Organic Molecules using Machine Learning & Causal Inference_

<br/>

---

`SMILES → Features → Prediction → Causal Design`

---

<br/>

[![Python](https://img.shields.io/badge/Python_3.8+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![RDKit](https://img.shields.io/badge/RDKit-Chemistry-1a1a2e?style=flat-square)](https://rdkit.org)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![EconML](https://img.shields.io/badge/EconML-Causal_Inference-8B0000?style=flat-square)](https://github.com/microsoft/EconML)
[![Gradio](https://img.shields.io/badge/Gradio-Web_App-FF7C00?style=flat-square)](https://gradio.app)
[![Status](https://img.shields.io/badge/Status-Active-2d6a4f?style=flat-square)](.)

</div>

<br/>

---

## What This Project Does

> Instead of spending days in the lab measuring molecular properties, type in a molecule's structure and get instant predictions.

**Input:** `c1ccccc1` _(Benzene SMILES)_

**Output:**

```
HOMO          →  -5.54 eV
LUMO          →  -3.89 eV
Optical Bandgap  →   1.46 eV
```

The pipeline goes further than prediction. Using causal inference, it can answer: _"If I modify this molecule's structure, what will actually change — and why?"_

---

## Table of Contents

- [Results at a Glance](#results-at-a-glance)
- [Project Workflow](#project-workflow)
- [Data & Features](#data--features)
- [Training Strategy — Hybrid Split Method](#training-strategy--hybrid-split-method)
- [Models Evaluated](#models-evaluated)
- [Transfer Learning Experiment](#transfer-learning-experiment)
- [Visualizations](#visualizations)
- [Step 6 — Causal Inference & Molecular Design](#step-6--causal-inference--molecular-design)
- [Interactive App (Gradio)](#interactive-app-gradio)
- [Project Structure](#project-structure)
- [Setup & Usage](#setup--usage)
- [Limitations & Future Work](#limitations--future-work)
- [Team](#team)

---

## Results at a Glance

Our best model (Random Forest) achieved the following across both evaluation strategies:

| Property        | Random Split R² | Scaffold Split R² | Hybrid R² | MAE (eV) |
| --------------- | --------------- | ----------------- | --------- | -------- |
| HOMO            | **0.659**       | 0.020             | **0.340** | 0.065    |
| LUMO            | **0.385**       | 0.020             | **0.203** | 0.066    |
| Optical Bandgap | **0.642**       | −0.070            | **0.286** | 0.055    |

Random Forest was the best overall model across all three properties. The **hybrid R²** is the most honest estimate of real-world performance — sitting between the optimistic random split and the pessimistic scaffold split. The large generalization gaps (0.365–0.712) confirm the model performs well on structurally familiar molecules but has limited extrapolation ability to truly novel scaffolds.

---

## Project Workflow

<!-- 📷 INSERT IMAGE: Project workflow overview diagram (Step-by-step pipeline from SMILES input to causal design output) -->

```
  Raw Data (CSV)
       │
       ▼
  Step 1 ── Data Preparation & Cleaning
       │
       ▼
  Step 2 ── Feature Extraction (SMILES → Morgan Fingerprints, 2048-bit)
       │
       ▼
  Step 3 ── Model Training (LR · SVR · RF · XGBoost · Neural Network)
       │         └── Hybrid Scaffold + Random Split Evaluation
       ▼
  Step 4 ── Evaluation & Visualization (Best model analysis)
       │
       ▼
  Step 5 ── Gradio Prediction App (Interactive interface)
       │
       ▼
  Step 6 ── Causal Inference & Counterfactual Design
               └── Double Machine Learning (EconML) · Counterfactual Engine · Inverse Molecular Design
```

---

## Data & Features

- **Dataset:** 1,571 organic acceptor molecules with experimentally measured HOMO, LUMO, and Optical Bandgap values (eV)
- **Source:** Organic photovoltaic research publications
- **Important note:** Records represent donor–acceptor molecular pairs rather than fully independent observations. Identical molecular structures appear across multiple entries due to the combinatorial pairing design — meaning standard random-split cross-validation overestimates true generalization performance. This is explicitly addressed by the hybrid evaluation strategy.
- **Molecular Representation:** Morgan Fingerprints (radius = 2, 2048 bits) via RDKit
- **Additional Descriptors:** 12 interpretable structural features including molecular weight, LogP, aromatic ring count, conjugation length, EWG/EDG counts, thiophene subunit count, fluorine count, and heteroatom fraction

<!-- 📷 INSERT IMAGE: EDA visualizations — distribution of HOMO, LUMO, Bandgap values across the dataset -->

---

## Training Strategy — Hybrid Split Method

This is one of the most important contributions of this project.

Standard random train/test splits are optimistic — if structurally similar molecules end up in both train and test sets, the model looks better than it actually is on genuinely new molecules. Scaffold-only splits go to the other extreme, often creating test sets that are too dissimilar to give a fair performance estimate.

**We combined both:**

| Split Method            | What It Measures                                                                                 |
| ----------------------- | ------------------------------------------------------------------------------------------------ |
| Random Split            | Upper bound — best-case performance on similar molecules                                         |
| Scaffold Split          | Lower bound — performance on structurally novel scaffolds                                        |
| **Hybrid Split (ours)** | **Realistic estimate — simple average of random and scaffold R², balancing both extremes**       |

The hybrid method gives a more honest and stable R² estimate. Prior work reported only random-split R² values, which our results show overestimate true generalization by **0.37–0.71 R² units** relative to scaffold splits. The hybrid metric avoids both the optimism of random-only evaluation and the excessive pessimism of scaffold-only evaluation.

<!-- 📷 INSERT IMAGE: Comparison chart — Random vs Scaffold vs Hybrid split R² scores across models -->

---

## Models Evaluated

Five model families were trained and compared:

| Model                | Random R² (HOMO) | Notes                                                        |
| -------------------- | ---------------- | ------------------------------------------------------------ |
| Linear Regression    | −0.143           | Failed entirely — molecular property relationships are non-linear |
| SVR (RBF kernel)     | 0.317            | Solid on small datasets                                      |
| **Random Forest**    | **0.659**        | **Best overall — wins on HOMO, LUMO, and Bandgap**           |
| XGBoost              | 0.365            | Competitive but did not consistently outperform RF           |
| Neural Network (MLP) | −5.410           | Catastrophic overfitting — insufficient data (needs 10,000+ samples) |

**Key observation:** Model complexity does not correlate with performance when the dataset is small. Random Forest outperforms all other models here because it is less prone to overfitting on 1,571 samples. Neural Networks overfitted catastrophically with a HOMO R² of −5.41 under random split, confirming they are not appropriate for this data regime without pre-training on a larger corpus.

<!-- 📷 INSERT IMAGE: Model performance comparison — R² and MAE across all 5 models for each property -->

---

## Transfer Learning Experiment

To address the dataset size limitation, we explored **transfer learning**: pre-training a neural network on a larger molecular property dataset, then fine-tuning on our 1,571-molecule acceptor dataset.

The approach did not outperform the hybrid split Random Forest baseline. Likely reasons:

- The pre-training domain had different molecular diversity than organic acceptors
- Fine-tuning on such a small dataset still leads to overfitting
- Tree-based methods with Morgan fingerprints remain better suited to this data regime

Transfer learning remains a promising direction if a larger, domain-matched pre-training corpus is assembled. The current results establish a clear benchmark to beat.

---

## Visualizations

### Data Distributions

<!-- 📷 INSERT IMAGE: EDA_visualizations — histograms of HOMO, LUMO, Bandgap; correlation matrix; molecule count per scaffold family -->

### Model Performance — Predicted vs Actual

<!-- 📷 INSERT IMAGE: model_performance — scatter plots of predicted vs actual values for HOMO, LUMO, Bandgap (best models) -->

### Split Strategy Comparison

<!-- 📷 INSERT IMAGE: Split comparison visualization — side-by-side bars for random / scaffold / hybrid split performance per model -->

---

## Step 6 — Causal Inference & Molecular Design

> Standard ML models learn _correlations_. The problem: correlations can be misleading.
>
> Example: Nitro groups correlate with low HOMO. But is it the nitro group causing it — or is it that nitro-containing molecules also tend to have longer conjugation? A correlation model cannot distinguish the two, and will fail when applied to new scaffolds.

We built three tools to go beyond correlation:

---

### Double Machine Learning (DML)

We used **EconML's LinearDML estimator** (Chernozhukov et al., 2018) to estimate the true causal effect of five pre-specified structural features on each electronic property — after controlling for confounders.

The confounder matrix was constructed by compressing 2,048-bit Morgan fingerprints to 100 components via SVD, appending 7 interpretable structural features, then applying PCA to retain 95.1% of total variance (94 principal components). Treatment variables used **Hammett sigma-para weighted EWG/EDG scores** rather than simple group counts, to account for the differential electron-withdrawing and donating strengths of individual functional groups. DML was executed with 10-fold cross-fitting.

All five tested causal relationships were **directionally consistent with published organic electronics literature**, but none survived Benjamini-Hochberg FDR correction at q < 0.05 — an honest finding driven by the small dataset size rather than a failure of the method. The Conjugation → Bandgap relationship passed a 100-permutation placebo test (true |ATE| = 0.256 >> 95th percentile threshold of 0.038), confirming the DML pipeline is functioning correctly.

<!-- 📷 INSERT IMAGE: causal_graph.png — DAG with blue feature nodes, red property nodes, orange confounder node (Mol. Weight) -->

---

### Causal Effects Heatmap

Estimated causal effects of each structural feature on each electronic property, after controlling for confounders.

<!-- 📷 INSERT IMAGE: causal_effects_heatmap.png — heatmap matrix of features × properties, red = raises, blue = lowers, values in eV -->

Red cells indicate that a feature raises the property value. Blue cells indicate it lowers it. All numbers are in eV after confounding removal.

---

### Causal vs Correlation Comparison

Where the correlation estimate and the causal estimate diverge significantly, the raw correlation was confounded. This chart makes those gaps visible.

<!-- 📷 INSERT IMAGE: causal_vs_correlation.png — side-by-side bar chart, grey = correlation, red = true causal effect, per feature/property pair -->

---

### Counterfactual Analysis

_"What would happen to this molecule's properties if I made this specific structural change?"_

The model predicts both the original molecule and the modified version, then reports **Δ = causal effect of the intervention** — not a raw correlation. Explicit reliability warnings are shown for fragile causal estimates, ensuring design recommendations are only drawn from statistically robust relationships.

<!-- 📷 INSERT IMAGE: counterfactual_effects.png — bar chart of Δ HOMO, Δ LUMO, Δ Bandgap for each available intervention -->

**Available interventions:**

- Thiophene → Benzene _(removes sulfur atom)_
- Benzene → Thiophene _(adds sulfur, lowers LUMO)_
- Add Fluorine _(electron-withdrawing group — lowers HOMO & LUMO)_
- Add Cyano group _(strong EWG — widens bandgap)_

---

### Inverse Design — Target a Specific Bandgap

Given a **target bandgap value**, the model ranks all structural modifications by how close they bring the molecule to that target. This transforms the system from a passive screening tool into an active **molecular design assistant**.

**Example — Target: 1.5 eV** _(relevant for organic solar cell absorbers)_

<!-- 📷 INSERT IMAGE: inverse_1.5eV.png — horizontal bar chart ranking modifications by proximity to 1.5 eV, green bar = best match, red dashed line = target -->

**Example — Target: 2.2 eV** _(relevant for blue/green OLED emitters)_

<!-- 📷 INSERT IMAGE: inverse_2.2eV.png — horizontal bar chart ranking modifications by proximity to 2.2 eV, green bar = best match, red dashed line = target -->

---

## Interactive App (Gradio)

We built a web interface using Gradio that requires no coding to use (~80 lines of Python).

**Features:**

- Paste any SMILES string and get predictions instantly
- View the 2D molecular structure rendered from the SMILES
- Compare predictions against dataset averages
- Counterfactual analysis tab with explicit reliability warnings
- Accessible from any device via a public shareable link

<!-- 📷 INSERT IMAGE: Gradio app screenshot 1 — main prediction interface -->
<!-- 📷 INSERT IMAGE: Gradio app screenshot 2 — molecular structure rendering output -->
<!-- 📷 INSERT IMAGE: Gradio app screenshot 3 — comparison with dataset statistics -->

---

## Project Structure

```
molecular-property-prediction/
│
├── Step_1_Data_Preparation.ipynb          — Merge, clean, and validate raw data
├── Step_2_Feature_Extraction.ipynb        — SMILES → Morgan Fingerprints + descriptors
├── Step_3_Model_Training.ipynb            — Train LR, SVR, RF, XGBoost, Neural Network
│                                             └── Hybrid scaffold + random split evaluation
├── Step_4_Evaluation_Visualization.ipynb  — Deep analysis of best models
├── Step_5_Prediction_Tool_Gradio.ipynb    — Interactive Gradio web application
├── Step_6_Causal_Inference.ipynb          — DML causal inference, counterfactuals, inverse design
│
├── Data_files/                            — Input CSV datasets
│
└── Each_Step_Output_Download/
    ├── models_rf.pkl                      — Trained Random Forest (best overall)
    ├── models_xgb.pkl                     — Trained XGBoost
    ├── models_svr.pkl                     — Trained SVR
    ├── causal_graph.png
    ├── causal_effects_heatmap.png
    ├── causal_vs_correlation.png
    ├── counterfactual_effects.png
    ├── counterfactual_results.csv
    ├── inverse_1.5eV.png
    └── inverse_2.2eV.png
```

---

## Setup & Usage

### Option 1 — Google Colab _(no setup required)_

1. Open any notebook in this repository
2. Click **Open in Colab**
3. Run cells in order using the ▶ button
4. Upload data when prompted — download results when done

---

### Option 2 — Local Installation

```bash
# Clone the repository
git clone https://github.com/Bsamuel-tech/molecular-property-prediction.git
cd molecular-property-prediction

# Install all dependencies
pip install rdkit pandas numpy scikit-learn tensorflow xgboost \
            gradio matplotlib seaborn econml networkx shap

# Launch the prediction app
cd Each_Step_Output_Download
python predict_gradio.py
```

The Gradio app will open in your browser and generate a public shareable link automatically.

---

## Limitations & Future Work

**Current limitations:**

- Models trained exclusively on acceptor molecules — not validated on donors
- Dataset records represent donor–acceptor pairs rather than fully independent molecules, inflating random-split performance
- Hybrid R² of ~0.28–0.34 leaves substantial variance unexplained; predictions are estimates, not ground truth
- Morgan fingerprints lose 3D spatial information (bond angles, conformational effects)
- Small dataset (1,571 records, ~605 unique acceptors) limits generalization to highly novel scaffolds
- No DML causal relationships survived FDR correction at the current sample size

**Planned improvements:**

- Expand to 5,000+ fully independent molecules to provide sufficient statistical power for stable causal estimation
- Adopt group-based cross-validation stratified by unique molecular identity to prevent information leakage
- Implement Graph Neural Networks (GNNs) which encode molecular topology directly
- Incorporate 3D conformational features (ETKDG-generated geometries)
- Incorporate donor-side structural features into the DML confounder matrix
- Train on donor molecules to cover the full organic semiconductor space
- Validate counterfactual predictions computationally using DFT (e.g., ORCA, Gaussian)
- Expand the modification library to 50+ structural transformations

---

## Technologies

| Area                 | Library              |
| -------------------- | -------------------- |
| Chemistry & Features | RDKit                |
| Machine Learning     | Scikit-learn         |
| Gradient Boosting    | XGBoost              |
| Deep Learning        | TensorFlow / Keras   |
| Causal Inference     | EconML (Microsoft)   |
| Model Explainability | SHAP                 |
| Web Interface        | Gradio               |
| Data Processing      | Pandas · NumPy       |
| Visualization        | Matplotlib · Seaborn |

---

## Team

Developed as an academic project in Machine Learning for Molecular Science.

**Sam · Yiming · Fredric**
_@ JUNIA ISEN_

Supervisor: **Dr. Kekeli N'KONOU**

---

## License

Free to use for academic learning and research purposes.

---

## Acknowledgments

- Dataset sourced from organic photovoltaic research literature
- RDKit open-source community for chemistry tooling
- Microsoft Research for the EconML causal inference framework
- Gradio team for making ML interfaces accessible without frontend engineering

---

<div align="center">

_Questions? Open an issue — the notebooks contain step-by-step explanations throughout._

**If this project was useful to you, consider leaving a star.**

</div>
