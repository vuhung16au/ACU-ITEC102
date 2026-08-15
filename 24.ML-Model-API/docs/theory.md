# Theory: Machine Learning APIs

## 1. Machine Learning Pipelines
A machine learning pipeline defines a sequence of data processing steps followed by a model. In this project, our pipeline scales numerical features (`StandardScaler`), one-hot encodes categorical features (`OneHotEncoder`), and finally passes the data to a `RandomForestRegressor`.

## 2. Model Serialization
After a model is trained, it exists in memory. To use it later (like in an API), we must save it to disk. We use `joblib` (or `pickle`) to serialize the trained `Pipeline` object into a file (e.g., `model.joblib`). When the API starts, it loads this file back into memory.

## 3. REST APIs for ML
A REST API allows different applications to communicate. By exposing our ML model via a `POST` endpoint using `FastAPI`, a frontend web application or mobile app can send user inputs (features) to the server, and the server returns the predicted value in JSON format.
