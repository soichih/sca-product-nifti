#!/bin/env python
import os
import json
import sys
import glob
import path
import errno
#import requests

#dump env .. for debuggin
for e in os.environ:
    if e.startswith("SCA_"):
        print e, os.environ[e]

#load config.json
config_json=open("config.json").read()
config=json.loads(config_json)

dir=config["source_dir"]

#karst has 2 issues 
#1. I need to do "pip install requests" to use requests
#2. (already fixed?) /N/soft/rhel6/python/2.7.3/lib/python2.7/site-packages/requests/packages/urllib3/util/ssl_.py:315: SNIMissingWarning: An HTTPS request has been made

#just look for .nii (or .nii.gz) in the source_dir and create symlinks
niifiles = []
for root, dirs, files in os.walk("../"+dir):
    for file in files:
        if file.endswith(".nii") or file.endswith(".nii.gz"):
            print file
            try:
                os.symlink("../"+dir+"/"+file, file) 
            except OSError, e:
                if e.errno == errno.EEXIST:
                    print "link already exists.. removing first"
                    os.remove(file)
                    os.symlink("../"+dir+"/"+file, file) 

            niifiles.append({"filename": file, "size": os.path.getsize("../"+dir+"/"+file)})

#output products.json
with open('products.json', 'w') as out:
    json.dump([{"type": "nifti", "files": niifiles}], out)

