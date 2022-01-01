from src import get_data
from src import write_data


iss_location = get_data.get_iss_location()
file_staged = write_data.write_locally(iss_location)
write_data.upload_blob("iss_test", 
                       f"data/{file_staged}", 
                       f"iss_5min/{file_staged}")
print(file_staged)

