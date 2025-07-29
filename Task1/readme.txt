# 🚂 Project: Data Pipeline Development (ETL)

This project demonstrates a basic **ETL (Extract, Transform, Load)** pipeline using Python for the **Titanic dataset**.  
The pipeline extracts the raw dataset, applies preprocessing steps, and outputs a cleaned CSV file ready for analysis or modeling.

---

## 🛠️ Tools & Libraries Used

- `pandas` – For data manipulation and extraction
- `scikit-learn` – For pipeline and preprocessing:
  - `Pipeline`
  - `SimpleImputer`
  - `LabelEncoder`
  - `StandardScaler`

---

## 🔄 ETL Steps Performed

### 1. **Extract**
- Loaded the **raw Titanic dataset** from `titanic.csv`.

### 2. **Transform**
- Dropped irrelevant columns like `Name`, `Ticket`, and `Cabin`.
- Preprocessing steps applied:
  - **Imputation**: Filled missing numeric values using the **mean**.
  - **Scaling**: Standardized numeric features using `StandardScaler`.
  - **Encoding**: Transformed categorical variables using `LabelEncoder`.

### 3. **Load**
- Merged transformed features with the target (`Survived`).
- Saved the cleaned dataset as `processed_titanic.csv`.

---

## 📦 How to Use

1. **Ensure Requirements**  
   - Python 3.x  
   - Install dependencies:  
     ```bash
     pip install pandas scikit-learn
     ```

2. **Place Files**  
   - Make sure the raw `titanic.csv` file is in the **same directory** as the script.

3. **Run the ETL Script**  
   ```bash
   python etl_pipeline.py
