from src import get_data
from src import write_data
import os

from flask import Flask

app = Flask(__name__)

@app.route("/")
def run():
    iss_location = get_data.get_iss_location()
    file_staged = write_data.write_locally(iss_location)
    write_data.upload_blob("iss_test", 
                        f"data/{file_staged}", 
                        f"iss_5min/{file_staged}")
 
    return ('', 204)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))