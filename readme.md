# 🌾 Crop Yield Prediction Project

This project involves a complete **data science and machine learning pipeline** to predict crop yield (hg/ha) using features such as **average rainfall, temperature, pesticide usage, crop type, and country**. Various regression models were compared, and the best-performing model was exported for deployment.

---

## 📊 Dataset Overview

| Feature                         | Description                            |
| ------------------------------- | -------------------------------------- |
| `Area`                          | Country name                           |
| `Item`                          | Type of crop (e.g. Wheat, Maize, etc.) |
| `Year`                          | Year of data                           |
| `hg/ha_yield`                   | Crop yield (target variable)           |
| `average_rain_fall_mm_per_year` | Average rainfall (mm/year)             |
| `pesticides_tonnes`             | Pesticides used (in tonnes)            |
| `avg_temp`                      | Average annual temperature (Celsius)   |

* Initial rows: **28,242**
* Final cleaned rows: **25,932**

---

## 🚮 Data Cleaning Highlights

* Removed `Unnamed: 0` column
* Handled missing values and validated numerical types
* Dropped **2310 duplicate records**
* Explored distribution using Seaborn plots

---

## 📊 Exploratory Data Analysis (EDA)

* Yield distribution across **countries** and **crop types** visualized using bar plots
* Top 3 highest yield crops:

  * Potatoes
  * Sweet potatoes
  * Cassava
* Yield analysis done per `Item` and `Area`

---

## 📅 Feature Engineering

* Selected key features:

  * `Year`, `average_rain_fall_mm_per_year`, `pesticides_tonnes`, `avg_temp`, `Area`, `Item`
* Target: `hg/ha_yield`
* Applied preprocessing using `ColumnTransformer`:

  * `OneHotEncoding` for categorical (`Area`, `Item`)
  * `StandardScaler` for numeric features

---

## 🔧 Models Used & Performance

| Model             | Mean Absolute Error (MAE) | R2 Score |
| ----------------- | ------------------------- | -------- |
| Linear Regression | 29,920.77                 | 0.75     |
| Lasso             | 29,907.60                 | 0.75     |
| Ridge             | 29,875.65                 | 0.75     |
| Decision Tree     | **4,206.54**              | **0.98** |
| KNN               | 4,869.09                  | 0.98     |

> ✅ **Decision Tree Regressor** performed the best and was chosen for deployment.

---

## 🔮 Predicting Crop Yield (Example)

```python
from predict import predict_yield

predict_yield([2023, 1200, 50, 30, 'Pakistan', 'Wheat'])
# Output: 27957.0 hg/ha
```

---

## 🚀 Deployment

The following assets are exported using `pickle` for easy deployment in web apps (e.g., FastAPI):

* `website/crop_yield_model.pkl`  → Trained Decision Tree model
* `website/crop_yield_preprocessor.pkl` → Preprocessing pipeline

---

## 🧰 Tech Stack

* **Pandas, NumPy** – Data manipulation and analysis
* **Seaborn, Matplotlib** – Visualizations
* **Scikit-learn** – Preprocessing, regression models, metrics
* **Pickle** – Saving models for deployment

---

## 📂 Project Structure

```
.
├── yield_df.csv                  # Raw dataset
├── crop_yield.ipynb             # Full notebook
├── predict.py                   # yield prediction function
├── website/
│   ├── crop_yield_model.pkl     # Exported Decision Tree model
│   └── crop_yield_preprocessor.pkl  # Exported ColumnTransformer
```

---

## 📉 Future Improvements

* [ ] Add rainfall forecasts and satellite vegetation index
* [✅] Deploy via **FastAPI**
* [ ] Add dynamic crop recommendation based on yield optimization

---

## 🙌 Acknowledgments

Developed by [Haris Ahmed](https://www.linkedin.com/in/haris-ahmed-785480257/) as part of AI/ML project portfolio. Data cleaned, analyzed, modeled, and deployed end-to-end.
