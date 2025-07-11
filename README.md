# Real-Time Transaction Anomaly Detector

This project is a real-time fraud detection system built using Apache Spark, designed to process streaming transaction logs and detect anomalies with high precision. An alert system is integrated into a web dashboard for monitoring in real-time.

## Features

- Spark-based streaming anomaly detection
- ROC curve optimization for threshold tuning
- Real-time alert dashboard using Dash
- SQL backend integration
- Achieved 87% precision on test data

## Structure

- `data/`: Example datasets and transaction logs
- `notebooks/`: Jupyter notebooks for experimentation and EDA
- `src/`: Source code for data pipeline and model
- `dashboard/`: Dash app for visualization and alerting
- `models/`: Saved models and thresholds

## How to Run

1. Start the Spark streaming job from `src/streaming_detector.py`
2. Launch the dashboard using `python dashboard/app.py`
3. Monitor real-time anomalies on the dashboard

