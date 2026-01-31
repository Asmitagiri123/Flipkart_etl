import sys
# Step 1: add your ETL project folder to Python path
sys.path.append("/home/asmita/Projects/flipkart_etl")

# Step 2: import your ETL functions
from extract import extract_flipkart_data
from transform import transform_data
from load import load_to_csv
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator


# Define default arguments
default_args = {
    'owner': 'asmita',
    'depends_on_past': False,
    'retries': 1,
}

# Define the DAG
with DAG(
    dag_id='flipkart_etl',
    default_args=default_args,
    start_date=datetime(2026, 1, 30),  # change to today's date or when you want DAG to start
    schedule_interval='@daily',  # runs once a day
    catchup=False,
    tags=['ETL', 'Flipkart'],
) as dag:

    # Step 1: Extract
    def extract_task():
        return extract_flipkart_data()

    # Step 2: Transform
    def transform_task(**context):
        raw_data = context['ti'].xcom_pull(task_ids='extract')
        return transform_data(raw_data)

    # Step 3: Load
    def load_task(**context):
        df = context['ti'].xcom_pull(task_ids='transform')
        load_to_csv(df, "mobiles_under_50000.csv")

    # Define tasks
    t1 = PythonOperator(
        task_id='extract',
        python_callable=extract_task
    )

    t2 = PythonOperator(
        task_id='transform',
        python_callable=transform_task,
        provide_context=True
    )

    t3 = PythonOperator(
        task_id='load',
        python_callable=load_task,
        provide_context=True
    )

    # Set task dependencies
    t1 >> t2 >> t3
