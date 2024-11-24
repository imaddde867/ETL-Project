# ETL Pipeline for Historical Weather Data

## Project Overview
This project is an automated ETL pipeline for processing historical weather data using Apache Airflow. It includes steps for extracting, transforming, validating, and loading the weather data. The pipeline ensures data quality and consistency through various validation checks.

### Features:
- Extracts weather data from a CSV file.
- Transforms data by calculating averages, mode, and categorizing wind strength.
- Validates data for missing values, range violations, and outliers.
- Logs errors and successful validations.
- Loads cleaned and validated data into an SQLite database.

## How to Run the ETL Pipeline

### Requirements
1. **Python 3.7+**  
2. **Apache Airflow**  
3. **pandas**  

Install the dependencies by running:

```bash
    pip install -r requirements.txt
```

## How to Run:
To run the ETL pipeline, ensure that **Airflow** is set up on your machine. Once set up:

1. Setting up Apache Airflow
Set the Airflow home directory:
```bash
export AIRFLOW_HOME=~/airflow
```
2. Install Apache Airflow:
```bash
pip install apache-airflow
```
3. Initialize the Airflow database:
```bash
airflow db init
```
4. Start the Airflow web server and scheduler:
```bash
airflow webserver --port 8080
airflow scheduler
```
5. Access the Airflow UI at http://localhost:8080.