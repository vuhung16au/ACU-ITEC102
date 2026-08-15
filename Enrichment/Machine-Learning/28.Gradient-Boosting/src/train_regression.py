import xgboost as xgb
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import root_mean_squared_error, r2_score
from data_fetcher import get_housing_data

def train_and_evaluate():
    print("Fetching Housing Data (Regression)...")
    df = get_housing_data()
    
    # Define features (X) and target (y)
    X = df.drop(columns=['price'])
    y = df['price']
    
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    print(f"\nTraining on {len(X_train)} samples, testing on {len(X_test)} samples.")
    print("Note: The dataset only has 'sale_year', 'small_area', and 'type'.")
    print("Without features like bedrooms or land size, the model's R2 score will naturally be very low!")
    
    # --- XGBoost ---
    print("\nTraining XGBoost Regressor...")
    xgb_model = xgb.XGBRegressor(
        objective='reg:squarederror',
        n_estimators=300, # Increased for slight tuning
        learning_rate=0.05, # Decreased for slight tuning
        max_depth=6, # Increased
        random_state=42
    )
    xgb_model.fit(X_train, y_train)
    xgb_preds = xgb_model.predict(X_test)
    
    xgb_rmse = root_mean_squared_error(y_test, xgb_preds)
    xgb_r2 = r2_score(y_test, xgb_preds)
    print(f"XGBoost RMSE: ${xgb_rmse:,.2f}")
    print(f"XGBoost R2 Score: {xgb_r2:.4f}")
    
    # --- LightGBM ---
    print("\nTraining LightGBM Regressor...")
    lgb_model = lgb.LGBMRegressor(
        objective='regression',
        n_estimators=300, # Increased for slight tuning
        learning_rate=0.05, # Decreased for slight tuning
        max_depth=6, # Increased
        random_state=42,
        verbosity=-1
    )
    lgb_model.fit(X_train, y_train)
    lgb_preds = lgb_model.predict(X_test)
    
    lgb_rmse = root_mean_squared_error(y_test, lgb_preds)
    lgb_r2 = r2_score(y_test, lgb_preds)
    print(f"LightGBM RMSE: ${lgb_rmse:,.2f}")
    print(f"LightGBM R2 Score: {lgb_r2:.4f}")
    
    print("\nRegression training complete.")

if __name__ == "__main__":
    train_and_evaluate()
