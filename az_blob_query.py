# from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os
import sys
from dotenv import load_dotenv
from pathlib import Path
import os.path
import pandas as pd

dotenv_path = Path('.env')
load_dotenv(dotenv_path=dotenv_path)

container_name = "analytics-playground-data-storage"
connection_string = "DefaultEndpointsProtocol=https;AccountName=microservicesstoreafrdev;AccountKey=1sZeV2d35MKBGM4wneLOt+cQH0mXcFJgvd19BnjcQk1vzh12xgg9loLzgIZSLcHjerlOEIQlc/L/1i1vCGR5vA==;EndpointSuffix=core.windows.net"
#os.getenv('_connection_string')

def config_csv_blob_upload(blob_name,file_path):
    blob_service_client = BlobServiceClient.from_connection_string(
            conn_str=connection_string, container_name=container_name, blob_name=blob_name)
    blob_client = blob_service_client.get_blob_client(container_name, blob_name)
    csv_file = Path(str(file_path))
    if os.path.isfile(csv_file):
        with open(csv_file, "rb") as data:
                blob_client.upload_blob(data,overwrite=True)      

def read_data_from_blob(blob_name,connection_string=connection_string):
    blob_service_client = BlobClient.from_connection_string(
        conn_str=connection_string, container_name=container_name, blob_name=blob_name)
    with open(blob_name, "wb") as f:
        data = blob_service_client.download_blob()
        data.readinto(f)
    return pd.read_csv(blob_name,low_memory=False)

def store_csv_in_dict(data_folder):
    blob_dict = {}
    for file in os.listdir(data_folder):
        blob_dict.update({str(file):os.path.join(data_folder,file)})
    return blob_dict

def upload_csv_data(data_folder='data'):
    blob_dict = store_csv_in_dict(data_folder)
    for k,v in blob_dict.items():
        try:
            config_csv_blob_upload(blob_name=k,file_path=v)
            print(f'File successfully uploaded: \n {k} - \n Shape {read_data_from_blob(blob_name=k).shape}')
        except BaseException:
            # Need more test cases for other errors
            print(f'Blob storage already exists for: \n {k}: Shape {read_data_from_blob(blob_name=k).shape}')

def main():
    upload_csv_data()

if __name__ == "__main__":
    main()