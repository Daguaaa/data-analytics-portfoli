# 🚕 Urban Surge Pricing: Predictive Modeling & BI Analysis
[Click here to view the full Python implementation and model training pipeline](https://colab.research.google.com/drive/106BhGKNviUYpHXl7mlCUuj7N9H_bLzHB?usp=sharing)

### 🎯 Project Objective
To build a machine learning system that identifies ride-sharing surge pricing events while maximizing user experience by reducing "false-alarm" surge alerts through high-precision modeling.

---

### 🛠️ The Technical Challenge
* **The Problem:** Initial baseline models suffered from feature leakage (bias toward car types) and high false-positive rates, leading to "surge fatigue."
* **The Solution:** * Removed biased features (Car Names/Brands).
    * Engineered **Spatial-Temporal Hubs** (linking specific locations to time-bins).
    * Implemented **Precision-Recall Optimization**, shifting the decision threshold to **0.81** to ensure high-confidence alerts.

---

### 📈 Key Business Insights
* **The "Surge Superhighways":** Surge events are highly concentrated in specific corridors, primarily **Back Bay ➔ Boston University** and **Back Bay ➔ Fenway**.
* **The Urban Heartbeat:** Discovered a predictable surge spike during the **Wednesday midnight transition (Hour 0)**, likely driven by mid-week shift changes at transport hubs.
* **Model Impact:** The final Random Forest model targets high-demand corridors with significantly improved precision, maintaining a seamless experience for **94% of total rides**.

---

### 🧪 Tech Stack
* **Language:** Python
* **Libraries:** Scikit-Learn, Pandas, Seaborn, Matplotlib
* **Model:** Random Forest Classifier (Balanced Weights)
* **Strategy:** Precision-Recall Curve & Threshold Tuning
