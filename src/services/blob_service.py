from typing import Any

import streamlit as st
from azure.storage.blob import BlobServiceClient

from utils.Config import Config


def upload_file_to_blob_storage(local_file_path: str, blob_name: str) -> Any | None:
    try:
        blob_service_client = BlobServiceClient.from_connection_string(
            Config.AZURE_STORAGE_CONNECTION_STRING
        )
        blob_client = blob_service_client.get_blob_client(
            container=Config.CONTAINER_NAME, blob=blob_name
        )
        blob_client.upload_blob(local_file_path, overwrite=True)
        return blob_client.url
    except Exception as e:
        st.write(f"Falha ao enviar o arquivo  {local_file_path} para o Azure Blob Storage. Erro: {str(e)}")
        return None