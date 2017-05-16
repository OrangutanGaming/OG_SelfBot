import json
import os

cDir = os.path.dirname(os.path.abspath(__file__))
with open(f"{cDir}/settings.json") as data_file:
    settings = json.load(data_file)
    data_file.close()

token = settings["token"]
password = settings["password"]

if token == "":
    print("No Token Given")
    exit()