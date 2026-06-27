from datetime import datetime, timedelta
from airflow.decorators import dag, task
from python_etl.scripts.download_dataset import download_dataset
from python_etl.scripts.untar_dataset import untar_dataset
from python_etl.scripts.extract_data_from_csv import extract_data_from_csv
from python_etl.scripts.extract_data_from_tsv import extract_data_from_tsv
from python_etl.scripts.extract_data_from_fixed_width import extract_data_from_fixed_width
from python_etl.scripts.consolidate_data import consolidate_data

default_args = {
    'owner': 'Marco Antonio',
    'start_date': datetime(2026, 6, 26),
    'email': ['rmarcoa098@gmail.com'],
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

@dag(
    dag_id="final_project",
    default_args=default_args,  # Se inyectan los argumentos por defecto
    schedule_interval=None,     # En 2.0 se usaba 'schedule_interval' en vez de 'schedule'
    catchup=False,
    description="Dag del módulo"
)
def mi_pipeline():
    @task
    def download():
        return download_dataset(
            source = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz',
            destination = '/home/project/airflow/dags/python_etl/staging/tolldata.tgz')

    first_task = download()
                            

mi_pipeline()