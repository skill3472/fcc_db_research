import requests
import os

file_name = "FCCdb_201130_v5_Zenodo.xlsx"

if os.path.isfile(file_name):
    print("The file " + file_name + " is already existing")
else:
    URL = "https://zenodo.org/record/4296944/files/FCCdb_201130_v5_Zenodo.xlsx"
    print("Starting download")
    response = requests.get(URL)
    open(file_name, "wb").write(response.content)
    print("Download complete")



