import json
import os

dir = os.path.dirname(os.path.abspath(__file__))
with open(f"{dir}/settings.json") as data_file:
    settings = json.load(data_file)

token = settings["token"]

if token == "":
    print("No Token Given")
    exit()