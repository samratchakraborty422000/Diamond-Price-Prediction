# 💎 Diamond Price Prediction using Machine Learning

This project predicts the price of diamonds based on their physical characteristics using various regression models including Decision Tree, Random Forest, XGBoost, and CatBoost. The final model is deployed with a simple **Streamlit** app.

---

## 📁 Dataset

The dataset contains 53,940 rows and 10 features about diamonds, including:

- **Carat** (Weight of the diamond)
- **Cut** (Quality of the cut: Ideal, Premium, etc.)
- **Color** (Grade from D to J)
- **Clarity** (SI2, VS1, IF, etc.)
- **Depth** (Total depth percentage)
- **Table** (Top width percentage)
- **Price** (Target variable - price in US dollars)
- **X, Y, Z** (Physical dimensions in mm)

There are **no missing values** in the dataset.

---

## 📊 Exploratory Data Analysis

- Used **Seaborn** and **Matplotlib** to visualize:
  - Relationship between price and features like cut, color, clarity
  - Scatter plots to observe correlation between carat and price
  - Bar plots to compare categorical features with price

---

## 🧹 Data Preprocessing

- Applied **Label Encoding** to convert categorical features (`Cut`, `Color`, `Clarity`) into numerical form.
- Split the dataset into training and testing sets (80% train, 20% test).
- Feature matrix: `X`
- Target variable: `y` (Price)

---

## 🤖 Models Used

### 1. **Decision Tree Regressor**
- MAE: `354.16`
- RMSE: `724.13`
- R² Score: `96.69%`

### 2. **Random Forest Regressor**
- MAE: `266.16`
- RMSE: `542.95`
- R² Score: `98.14%`

### 3. **XGBoost Regressor**
- MAE: `274.38`
- RMSE: `537.05`
- R² Score: `98.18%`

### 4. **CatBoost Regressor** ⭐️ (Best)
- MAE: `273.96`
- RMSE: `531.15`
- R² Score: `98.22%`

✅ **CatBoost outperformed all other models**, and is selected for deployment.

---
### Model Performance Summary

| Model                | MAE      | MSE         | RMSE     | R² Score  |
|----------------------|----------|-------------|----------|-----------|
| Decision Tree        | 354.16   | 524,367.04  | 724.13   | 0.967     |
| Random Forest       | 266.16   | 294,799.92  | 542.95   | 0.981     |
| XGBoost             | 274.39   | 288,425.16  | 537.05   | 0.982     |
| **CatBoost (Best)** | 273.97   | 282,121.88  | 531.15   | **0.982** |


## 🧠 Final Model: CatBoost Regressor

- Trained with `iterations=1000`, `learning_rate=0.05`, and `depth=6`
- Saved using `pickle`:

  ```python
  with open("catboost_model.pkl", "rb") as f:
    cat_loaded = pickle.load(f)

## 💻 Run the app locally:

Install required packages:

```bash
pip install -r requirements.txt
```

### Run the app:

```bash
streamlit run app.py
```
## Screenshots

<img width="1128" height="866" alt="image" src="https://github.com/user-attachments/assets/1db64ac0-4877-4579-babd-5af520cec408" />

<img width="1332" height="708" alt="image" src="https://github.com/user-attachments/assets/74cabaa6-3fde-48f9-91fa-73351ce7ddaa" />

