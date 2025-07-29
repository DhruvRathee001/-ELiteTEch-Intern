PROJECT: Data Pipeline Development (ETL)

TOOLS USED:
- pandas
- scikit-learn (Pipeline, SimpleImputer, LabelEncoder, StandardScaler)

STEPS PERFORMED:
1. Extracted raw Titanic dataset (CSV).
2. Dropped irrelevant columns.
3. Applied preprocessing:
   - Filled missing numeric values with mean.
   - Scaled numeric features.
   - Encoded categorical values with LabelEncoder.
4. Combined transformed features and target.
5. Saved clean data to processed_titanic.csv

USAGE:
- Run `etl_pipeline.py` using Python 3.
- Ensure `titanic.csv` is in the same folder.
