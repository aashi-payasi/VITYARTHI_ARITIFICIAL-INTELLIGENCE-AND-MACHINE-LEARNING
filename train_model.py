#train_model.py
import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import StandardScaler
import joblib

np.random.seed(42)

def generate_synthetic_data(n_normal=950, n_anomalies=50):
    normal_amount = np.random.normal(2000, 1200, n_normal).clip(50, 15000)
    normal_hour = np.random.normal(14, 4, n_normal).clip(0, 23)
    normal_day = np.random.randint(0, 7, n_normal)
    normal_balance = np.random.normal(25000, 10000, n_normal).clip(1000, 100000)
    normal_ratio = normal_amount / normal_balance

    anomaly_amount = np.random.uniform(15000, 60000, n_anomalies)
    anomaly_hour = np.random.choice([0, 1, 2, 3, 4, 23], n_anomalies)
    anomaly_day = np.random.randint(0, 7, n_anomalies)
    anomaly_balance = np.random.normal(20000, 8000, n_anomalies).clip(1000, 100000)
    anomaly_ratio = anomaly_amount / anomaly_balance

    df = pd.DataFrame({
        "amount": np.concatenate([normal_amount, anomaly_amount]),
        "hour": np.concatenate([normal_hour, anomaly_hour]),
        "dayofweek": np.concatenate([normal_day, anomaly_day]),
        "balance_before": np.concatenate([normal_balance, anomaly_balance]),
    })
    df["amount_to_balance_ratio"] = df["amount"] / df["balance_before"]
    return df

def main():
    df = generate_synthetic_data()
    df.to_csv("transaction_history.csv", index=False)
    print(f"Synthetic dataset created: {len(df)} rows -> transaction_history.csv")

    features = ["amount", "hour", "dayofweek", "balance_before", "amount_to_balance_ratio"]
    X = df[features].values

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    model = IsolationForest(n_estimators=200, contamination=0.05, random_state=42)
    model.fit(X_scaled)

    joblib.dump(model, "fraud_model.pkl")
    joblib.dump(scaler, "scaler.pkl")
    print("Model trained and saved -> fraud_model.pkl, scaler.pkl")

if __name__ == "__main__":
    main()
