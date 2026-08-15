import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler
import joblib
import os

MODEL_PATH = "data/model.joblib"
DATA_PATH = "data/mock_vehicles.csv"

def train_model():
    print("Loading data...")
    df = pd.read_csv(DATA_PATH)
    
    X = df[['Make', 'Engine_Size_L', 'Fuel_Type', 'Fuel_Consumption_L_100km']]
    y = df['CO2_Emissions_g_km']
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    numeric_features = ['Engine_Size_L', 'Fuel_Consumption_L_100km']
    numeric_transformer = StandardScaler()
    
    categorical_features = ['Make', 'Fuel_Type']
    categorical_transformer = OneHotEncoder(handle_unknown='ignore')
    
    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])
    
    pipeline = Pipeline(steps=[('preprocessor', preprocessor),
                               ('regressor', RandomForestRegressor(n_estimators=100, random_state=42))])
    
    print("Training model...")
    pipeline.fit(X_train, y_train)
    
    score = pipeline.score(X_test, y_test)
    print(f"Model R2 Score: {score:.4f}")
    
    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)
    joblib.dump(pipeline, MODEL_PATH)
    print(f"Model saved to {MODEL_PATH}")

def predict(features: dict):
    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(f"Model not found at {MODEL_PATH}. Please train the model first.")
        
    model = joblib.load(MODEL_PATH)
    df = pd.DataFrame([features])
    prediction = model.predict(df)[0]
    return float(prediction)

if __name__ == "__main__":
    train_model()
