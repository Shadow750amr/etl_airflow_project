
import requests


source = 'https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DB0250EN-SkillsNetwork/labs/Final%20Assignment/tolldata.tgz'
destination = '/home/project/airflow/dags/python_etl/staging/tolldata.tgz'

def download_dataset(source_path,destination_path):
    with requests.get(source_path, stream=True) as response:
        response.raise_for_status()
        with open(destination_path, "wb") as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

if __name__=="__main__":
    download_dataset(source,destination)

