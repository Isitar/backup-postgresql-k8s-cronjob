import os, uuid
import sys
import datetime
from azure.storage.blob import BlobServiceClient, __version__

try:
	print("Azure Blob Storage v" + __version__)

	container_name = 'postgresql-backups'

	connect_str = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
	blob_service_client = BlobServiceClient.from_connection_string(connect_str)

	# ensure blob container exists
	containers = blob_service_client.list_containers(name_starts_with=container_name)
	container_client = blob_service_client.get_container_client(container_name)
	if not container_client.exists():
		container_client.create_container()

	# uplaod file
	file_to_upload = sys.argv[1]
	current_time = datetime.datetime.now()
	blob_name = f"{current_time.year:04d}/{current_time.month:02d}/{current_time.day:02d}/{current_time.hour:02d}{current_time.minute:02d}{current_time.second:02d}-{os.path.basename(file_to_upload)}"
	print(f"Uploading {file_to_upload} to {container_name}/{blob_name}")

	blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)

	with open(file_to_upload, "rb") as data:
		blob_client.upload_blob(data)

	print(f"Uploaded {file_to_upload} to {container_name}")

except Exception as ex:
	print('Exception:')
	print(ex)
