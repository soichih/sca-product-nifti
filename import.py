#!/bin/env python
import os
import json
import sys
import glob
import requests

#dump env .. for debuggin
for e in os.environ:
    if e.startswith("SCA_"):
        print e, os.environ[e]

#load config.json
config_json=open("config.json").read()
config=json.loads(config_json)

dir=config["source_dir"]

#for file in config["files"]:
#    #print file["filename"]
#    #print file["type"]
#    status = "Checking "+file["filename"]
##    requests.post(os.environ["SCA_PROGRESS_URL"], data='{"status":"'+status+'"}')
#
#    #TODO - for now, I am just going to check for file extension.. In the future, I will implement something a bit more capable
#    if file["filename"].endswith(".nii"):
#        products[] = file

print "posting status update"
requests.post(os.environ["SCA_PROGRESS_URL"], json={"status":"Searching for .nii"})

#look for .nii in the source_dir and create symlinks
files = []
for file in glob.glob(config["source_dir"]+"/*.nii"):
    print "../"+config["source_dir"]+"/"+file
    os.symlink("../"+config["source_dir"]+"/"+file, file) 
    files.append({"filename": file})

#output products.json
with open('products.json', 'w') as out:
    json.dump({"files": files}, out)


