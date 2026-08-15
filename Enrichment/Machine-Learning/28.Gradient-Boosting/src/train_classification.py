import xgboost as xgb
import lightgbm as lgb
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, f1_score, classification_report
from data_fetcher import get_crash_data

def train_and_evaluate():
    print("Fetching Crash Data (Classification)...")
    df = get_crash_data()
    
    # Define features (X) and target (y)
    X = df.drop(columns=['is_injury'])
    y = df['is_injury']
    
    # Split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Calculate class imbalance ratio to pass to scale_pos_weight
    # ratio = count(negative class) / count(positive class)
    neg_count = sum(y_train == 0)
    pos_count = sum(y_train == 1)
    imbalance_ratio = neg_count / pos_count
    
    print(f"\nTraining on {len(X_train)} samples, testing on {len(X_test)} samples.")
    print(f"Class Distribution: {neg_count} Property Damage (0) vs {pos_count} Injuries (1). Ratio: {imbalance_ratio:.2f}")
    
    # --- XGBoost ---
    print("\nTraining XGBoost Classifier (with scale_pos_weight)...")
    xgb_model = xgb.XGBClassifier(
        objective='binary:logistic',
        n_estimators=100,
        learning_rate=0.1,
        max_depth=4,
        scale_pos_weight=imbalance_ratio, # Crucial for imbalanced data!
        random_state=42,
        eval_metric='logloss'
    )
    xgb_model.fit(X_train, y_train)
    xgb_preds = xgb_model.predict(X_test)
    
    print(f"XGBoost Accuracy: {accuracy_score(y_test, xgb_preds):.4f}")
    print(f"XGBoost F1-Score: {f1_score(y_test, xgb_preds):.4f}")
    
    # --- LightGBM ---
    print("\nTraining LightGBM Classifier (with scale_pos_weight)...")
    lgb_model = lgb.LGBMClassifier(
        objective='binary',
        n_estimators=100,
        learning_rate=0.1,
        max_depth=4,
        scale_pos_weight=imbalance_ratio, # Crucial for imbalanced data!
        random_state=42,
        verbosity=-1
    )
    lgb_model.fit(X_train, y_train)
    lgb_preds = lgb_model.predict(X_test)
    
    print(f"LightGBM Accuracy: {accuracy_score(y_test, lgb_preds):.4f}")
    print(f"LightGBM F1-Score: {f1_score(y_test, lgb_preds):.4f}")
    
    print("\nClassification training complete.")

if __name__ == "__main__":
    train_and_evaluate()
