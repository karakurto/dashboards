
from google.cloud import storage

from datetime import datetime, timedelta


bucket_name = 'knowledge-journal.appspot.com'
source_blob_name = 'visitors.html'
destination_file_name = '/tmp/visitors.html'
source_file_name = '/tmp/visitors.html'
destination_blob_name = 'visitors.html'

def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # source_blob_name = "storage-object-name"
    # destination_file_name = "local/path/to/file"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # bucket_name = "your-bucket-name"
    # source_file_name = "local/path/to/file"
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)

def visitor_tracker(request):

        request.session.create()
        session = request.session.session_key

        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')

        date = datetime.now()
        download_blob(bucket_name, source_blob_name, destination_file_name)
        with open(source_file_name, "a") as f:
            f.write(f"{session}: {date}: {ip}<br>")
        upload_blob(bucket_name, source_file_name, destination_blob_name)