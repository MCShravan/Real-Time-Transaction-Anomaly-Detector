import findspark
findspark.init()

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, from_json
from pyspark.sql.types import StructType, StringType, DoubleType
from sklearn.metrics import roc_curve
import joblib

# Initialize Spark session
spark = SparkSession.builder     .appName("RealTimeTransactionAnomalyDetector")     .getOrCreate()

# Define schema for incoming transactions
schema = StructType()     .add("transaction_id", StringType())     .add("amount", DoubleType())     .add("location", StringType())     .add("timestamp", StringType())     .add("label", StringType())  # 'normal' or 'fraud'

# Load streaming data (simulated with a folder)
streaming_df = spark.readStream     .schema(schema)     .json("data/")

# Load saved model and threshold
model = joblib.load("models/fraud_model.pkl")
threshold = joblib.load("models/optimal_threshold.pkl")

# Feature transformation and prediction
def predict_and_flag(batch_df, epoch_id):
    import pandas as pd
    df = batch_df.toPandas()
    if df.empty:
        return
    features = df[['amount']]  # Simplified example
    probs = model.predict_proba(features)[:, 1]
    df['prediction'] = (probs >= threshold).astype(int)
    df[['transaction_id', 'amount', 'prediction']].to_csv("dashboard/alerts.csv", mode='a', index=False)

streaming_df.writeStream     .foreachBatch(predict_and_flag)     .start()     .awaitTermination()
