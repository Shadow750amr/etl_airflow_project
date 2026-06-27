import pandas as pd 
from typing import Optional

file_path='/home/project/airflow/dags/python_etl/staging/tollplaza-data.tsv'
destination_path='/home/project/airflow/dags/python_etl/staging/tsv_data.csv'

def extract_data_from_tsv(file_path,destination_path:Optional[str]=None):
    df = pd.read_csv(file_path,sep='\t',header=None)
    columns = df.iloc[:,[4,2,5]]
    columns.columns = ['Number of axles','Tollplaza id','Tollplaza code']
    columns.to_csv(destination_path,index=False)
    print(columns.head(5))

    ##df.to_csv(destination_path)

if __name__=="__main__":
    extract_data_from_tsv(file_path=file_path,destination_path=destination_path)
