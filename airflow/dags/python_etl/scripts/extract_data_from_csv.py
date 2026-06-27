import pandas as pd 
from typing import Optional

file_path='/home/project/airflow/dags/python_etl/staging/vehicle-data.csv'
destination_path='/home/project/airflow/dags/python_etl/staging/csv_data.csv'

def extract_data_from_csv(file_path,destination_path:Optional[str]=None):
    df = pd.read_csv(file_path,header=None)
    columns = df.iloc[:,[0,1,2,3]]
    columns.columns = ['Rowid','Timestamp','Anonymized Vehicle number','Vehicle type']
    columns.to_csv(destination_path,index=False)
    print(columns.head(5))



if __name__=="__main__":
    extract_data_from_csv(file_path=file_path,destination_path=destination_path)
