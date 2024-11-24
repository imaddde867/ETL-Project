# ETL Pipeline for Historical Weather Data

## Project Overview
This project is an automated ETL pipeline for processing historical weather data using Apache Airflow. It includes steps for extracting, transforming, validating, and loading the weather data. The pipeline ensures data quality and consistency through various validation checks.

### Features:
- Extracts weather data from a CSV file.
- Transforms data by calculating averages, mode, and categorizing wind strength.
- Validates data for missing values, range violations, and outliers.
- Logs errors and successful validations.
- Loads cleaned and validated data into an SQLite database.

## Requirements
To run the project, you need to install the following dependencies:

- `pandas`: For data manipulation and validation.
- `apache-airflow`: For orchestrating the ETL pipeline.

To install the dependencies, use:

```bash
pip install -r requirements.txt
```

## How to Run:
To run the ETL pipeline, ensure that **Airflow** is set up on your machine. Once set up:

1. Run the Airflow webserver and scheduler.
2. Trigger the DAG via the Airflow UI to start processing the weather data.
3. Your validation process will be checked before any further steps proceed, as per your task requirements.
