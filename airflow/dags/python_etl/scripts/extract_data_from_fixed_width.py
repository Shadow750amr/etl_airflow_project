import pandas as pd 
from typing import Optional
import numpy as np
file_path='/home/project/airflow/dags/python_etl/staging/payment-data.txt'
destination_path='/home/project/airflow/dags/python_etl/staging/fixed_width_data.csv'

def extract_data_from_fixed_width(file_path,destination_path:Optional[str]=None):
    df = pd.read_csv(file_path,  sep=r'\s+',header=None)
    columns = df.iloc[:,[9,8]]
    columns.reset_index(inplace=True,drop=True)
    columns.columns = ["Type of payment", "Vehicle Code"]
    columns.to_csv(destination_path,index=False)
    print(columns.head())


    ##df.to_csv(destination_path)

if __name__=="__main__":
    extract_data_from_fixed_width(file_path=file_path,destination_path=destination_path)
