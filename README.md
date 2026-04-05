# Quantum Market Regime Detector — Team Structure & Responsibilities

---

## Team Roles & Responsibilities

### P1 — Data Engineer

**Goal:**
Build a clean, structured dataset for the entire pipeline.

**Responsibilities:**

* Fetch stock market data (NSE/BSE via yfinance or equivalent)
* Compute financial features:

  * Daily returns
  * Rolling correlation matrices
* Generate regime labels:

  * Bull (rising trend)
  * Bear (declining trend)
  * Crisis (high volatility)

**Deliverables:**

* `data/processed/features.csv`
* `data/labels/regimes.csv`

**Dependency Impact:**
This stage forms the foundation of the project. Errors here will propagate through all subsequent stages.

---

### P2 — Quantum Developer

**Goal:**
Transform classical financial data into a quantum-representable format and compute similarity.

**Responsibilities:**

* Implement amplitude encoding (map returns to qubit states)
* Design quantum circuits:

  * Feature map
  * Entanglement layers
* Construct quantum kernel function:

  * K(x, x')

**Deliverables:**

* Kernel matrix representing similarity between data points

**Dependency Impact:**
Provides the quantum representation required for model training.

---

### P3 — Machine Learning Engineer

**Goal:**
Train and evaluate models using both quantum and classical approaches.

**Responsibilities:**

* Train quantum model:

  * Variational Quantum Kernel (VQK)
* Build classical baselines:

  * Support Vector Machine (SVM)
  * Multi-layer Perceptron (MLP)
* Evaluate performance:

  * Accuracy
  * F1 Score

**Deliverables:**

* `metrics.json`
* Trained model files

**Dependency Impact:**
Determines the effectiveness of the approach and validates results.

---

### P4 — Backend Developer

**Goal:**
Expose the system through usable APIs.

**Responsibilities:**

* Build REST API (FastAPI/Flask)
* Implement endpoints:

  * `/predict` for regime prediction
  * `/upload-portfolio` for user input
* Load and serve trained models

**Deliverables:**

* Running backend API service

**Dependency Impact:**
Enables integration and real-world usability.

---

### P5 — Visualization Engineer

**Goal:**
Present outputs in a clear and interpretable format.

**Responsibilities:**

* Create visualizations:

  * Market regime timeline
  * Correlation heatmaps
* Build interactive dashboard (Streamlit)

**Deliverables:**

* Dashboard interface
* Visual outputs for reporting

**Dependency Impact:**
Improves interpretability and presentation quality.

---

## System Workflow

The system follows a sequential pipeline:

1. Data Engineering (P1)
   Collects and processes raw stock data into structured features and labels.

2. Quantum Processing (P2)
   Encodes data into quantum states and computes kernel similarities.

3. Model Training (P3)
   Uses quantum kernel and classical methods to train and evaluate models.

4. Backend Integration (P4)
   Exposes trained models via APIs.

5. Visualization (P5)
   Displays results through dashboards and plots.

---

## Data Flow

P1 → P2 → P3 → P4 → P5

---

## Key Considerations

* Maintain consistent data formats across modules (CSV, JSON)
* Each role should work within its designated module
* Outputs from one stage must be clearly defined for the next
* Integration should be incremental, not only at the end

---

## Summary

The project is designed as a modular system with clear separation of responsibilities.
Each role contributes independently while maintaining a structured flow of data and outputs across the pipeline.
