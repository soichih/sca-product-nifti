#!/bin/env python
import os
import json
import sys
import requests

#dump env .. for debuggin
for e in os.environ:
    print e, os.environ[e]

#load config.json
config_json=open("config.json").read()
config=json.loads(config_json)

products = []

for file in config["files"]:
    #print file["filename"]
    #print file["type"]
    status = "Checking "+file["filename"]
    requests.post(os.environ["SCA_PROGRESS_URL"], data='{"status":"'+status+'"}')

    #TODO - for now, I am just going to check for file extension.. In the future, I will implement something a bit more capable
    if file["filename"].endswith(".nii"):
        products[] = file

#output products.json
with open('products.json', 'w') as out:
    json.dump(products, out)


