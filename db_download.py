import requests
import os

# DB record
record_id = "4296944"
record_url = f"https://zenodo.org/record/{record_id}/files/"

# API call
response = requests.get(f"https://zenodo.org/api/records/{record_id}")
files = response.json()['files']

# Fetch
for file in files:
    if file['key']:
        if os.path.isfile(file['key']):
            print("The file " + file['key'] + "  already exists")
        else:
            print("Starting download")

            file_url = record_url + file['key']
            response = requests.get(file_url)

            with open(os.path.basename(file['key']), 'wb') as f:
                f.write(response.content)
            print("Download complete")
            break
    else:
        print("File could not be found")
