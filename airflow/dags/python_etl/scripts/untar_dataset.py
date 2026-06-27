import tarfile

original_path= '/home/project/airflow/dags/python_etl/staging/tolldata.tgz'
extract_destination= '/home/project/airflow/dags/python_etl/staging'

def untar_dataset(original_path,extract_destination):
    with tarfile.open(original_path, "r:gz") as tar:
        # Use filter='data' to protect against directory traversal security vulnerabilities
        tar.extractall(path=extract_destination, filter='data')


if __name__=="__main__":
    untar_dataset(original_path,extract_destination)