import pandas as pd 
from typing import Optional

file_path1 = '/home/project/airflow/dags/python_etl/staging/csv_data.csv'
file_path2 = '/home/project/airflow/dags/python_etl/staging/tsv_data.csv'
file_path3 = '/home/project/airflow/dags/python_etl/staging/fixed_width_data.csv'

destination_path = '/home/project/airflow/dags/python_etl/staging/extracted_data.csv'

def consolidate_data (file_path1: str, file_path2: str, file_path3: str, destination_path: Optional[str] = None) -> Optional[pd.DataFrame]:
    # 1. Leer los tres archivos locales
    df1 = pd.read_csv(file_path1)
    df2 = pd.read_csv(file_path2, sep='\t') 
    df3 = pd.read_csv(file_path3)           
    
    # 2. Hacer el concat de los DataFrames
    df_concatenado = pd.concat([df1, df2, df3], ignore_index=True)
    
    # 3. Definir el orden estricto de las columnas solicitado
    # Asegurate de que los nombres coincidan exactamente con los headers de tus archivos (Mayúsculas/Minúsculas)
    ordered_columns = [
        'Rowid', 
        'Timestamp', 
        'Anonymized Vehicle number', 
        'Vehicle type', 
        'Number of axles', 
        'Tollplaza id', 
        'Tollplaza code', 
        'Type of Payment code', 
        'Vehicle Code'
    ]
    
    # Reindexamos para forzar el orden exacto y descartar columnas extra si las hubiera
    df_final = df_concatenado.reindex(columns=ordered_columns)
    
    # 4. Guardar en el destino
    if destination_path:
        df_final.to_csv(destination_path, index=False)
        print(f"Data exitosamente ordenada y guardada en: {destination_path}")
        return None
    
    return df_final

if __name__ == "__main__":
    extract_data_from_csv(
        file_path1=file_path1, 
        file_path2=file_path2, 
        file_path3=file_path3, 
        destination_path=destination_path
    )