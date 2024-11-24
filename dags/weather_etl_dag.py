from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from scripts.data_validation import validate_weather_data

def validate_data_task(**kwargs):
    """
    Airflow task to validate data.
    """
    ti = kwargs['ti']
    file_path = 'data/weatherHistory.csv'  # Path to your dataset
    validate_weather_data(file_path)  # Call the validation function

# Define default arguments
default_args = {
    'owner': 'Imad',
    'start_date': datetime(2024, 11, 20),
    'retries': 1,
}

# Define DAG
dag = DAG('weather_data_etl', default_args=default_args, schedule_interval=None)

# Define tasks
validate_task = PythonOperator(
    task_id='validate_data_task',
    python_callable=validate_data_task,
    provide_context=True,
    dag=dag,
)