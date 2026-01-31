import sys

sys.path.append("/home/asmita/Projects/flipkart_etl")


from extract import extract_flipkart_data
from transform import transform_data
from load import load_to_csv
from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator



default_args = {
    'owner': 'asmita',
    'depends_on_past': False,
    'retries': 1,
}


with DAG(
    dag_id='flipkart_etl',
    default_args=default_args,
    start_date=datetime(2026, 1, 30),  # change to today's date or when you want DAG to start
    schedule_interval='@daily',  # runs once a day
    catchup=False,
    tags=['ETL', 'Flipkart'],
) as dag:

    
    def extract_task():
        return extract_flipkart_data()

    
    def transform_task(**context):
        raw_data = context['ti'].xcom_pull(task_ids='extract')
        return transform_data(raw_data)

    
    def load_task(**context):
        df = context['ti'].xcom_pull(task_ids='transform')
        load_to_csv(df, "mobiles_under_50000.csv")

    
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

    t1 >> t2 >> t3
