import pandas as pd

def validate_weather_data(file_path):
    """
    Validate the weather data for missing values, range violations, and outliers.
    param file_path: Path to the CSV file.
    return: None if validation passes, raises ValueError otherwise.
    """
    data = pd.read_csv(file_path)

    # Missing values check
    missing_columns = data.columns[data.isnull().any()]
    if not missing_columns.empty:
        raise ValueError(f"Missing values found in columns: {missing_columns.tolist()}")

    # Range checks
    if not data['Temperature (C)'].between(-50, 50).all():
        raise ValueError("Temperature values out of range.")
    if not data['Humidity'].between(0, 1).all():
        raise ValueError("Humidity values out of range.")

    # Outlier detection
    q1 = data['Temperature (C)'].quantile(0.25)
    q3 = data['Temperature (C)'].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = data[(data['Temperature (C)'] < lower_bound) | (data['Temperature (C)'] > upper_bound)]
    if not outliers.empty:
        print(f"Outliers detected:\n{outliers}")

    print("Validation successful!")


#Data logging

import logging

logging.basicConfig(filename='logs/validation_logs.txt', level=logging.INFO)

def validate_weather_data(file_path):
    """
    Validate the weather data for missing values, range violations, and outliers.

    :param file_path: Path to the CSV file.
    :return: None if validation passes, raises ValueError otherwise.
    """
    logging.info("Starting validation process.")
    data = pd.read_csv(file_path)

    # Missing values check
    missing_columns = data.columns[data.isnull().any()]
    if not missing_columns.empty:
        error_message = f"Missing values found in columns: {missing_columns.tolist()}"
        logging.error(error_message)
        raise ValueError(error_message)

    # Range checks
    if not data['Temperature (C)'].between(-50, 50).all():
        error_message = "Temperature values out of range."
        logging.error(error_message)
        raise ValueError(error_message)
    if not data['Humidity'].between(0, 1).all():
        error_message = "Humidity values out of range."
        logging.error(error_message)
        raise ValueError(error_message)

    # Outlier detection
    q1 = data['Temperature (C)'].quantile(0.25)
    q3 = data['Temperature (C)'].quantile(0.75)
    iqr = q3 - q1
    lower_bound = q1 - 1.5 * iqr
    upper_bound = q3 + 1.5 * iqr
    outliers = data[(data['Temperature (C)'] < lower_bound) | (data['Temperature (C)'] > upper_bound)]
    if not outliers.empty:
        logging.warning(f"Outliers detected:\n{outliers}")

    logging.info("Validation successful!")