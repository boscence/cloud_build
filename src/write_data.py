import csv

from datetime import datetime
from google.cloud import storage

def write_locally(returned_json):
    print(returned_json)
    now = datetime.now().strftime(format = '%Y%m%d_%H%M')

    csv_columns = ['latitude','longitude','timestamp']

    try:
        with open(f"data/iss_location_{now}.csv", 'w') as temp:
            writer = csv.DictWriter(temp, fieldnames=csv_columns)
            writer.writeheader()

            writer.writerow(returned_json)
    except IOError:
        print("I/O error")
    return f"iss_location_{now}.csv"





def upload_blob(bucket_name, 
                source_file_name, 
                destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )

