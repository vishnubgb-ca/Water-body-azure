import os
from azure.identity import ClientSecretCredential
from azure.storage.blob import BlobServiceClient
from datetime import datetime, timedelta
from azure.storage.blob import generate_blob_sas, BlobSasPermissions

def extract_data():
    client_id = os.environ["client_id"]
    client_secret = os.environ["client_secret"]
    tenant_id = os.environ["tenant_id"]
    account_url = os.environ["account_url"]
    default_credential = ClientSecretCredential(client_id=client_id,client_secret=client_secret,tenant_id=tenant_id)
    blob_service_client = BlobServiceClient(account_url, credential=default_credential)
    container_client = blob_service_client.get_container_client("deeplearning-mlops")
    account_key = os.environ["account_key"]
    permissions = BlobSasPermissions(read=True)
    sas_token = generate_blob_sas(
                    account_name=os.environ["account_name"],
                    container_name="deeplearning-mlops",
                    blob_name='Water_Bodies_Dataset_Split.zip',
                    account_key=account_key,  
                    permission=permissions,
                    expiry=datetime.utcnow() + timedelta(hours=1),  
                )
    url = f"{account_url}/deeplearning-mlops/Water_Bodies_Dataset_Split.zip?{sas_token}"
    print(url)
    return url

extract_data()
