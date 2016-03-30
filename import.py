#!/bin/env python
import os
import json
import sys

#dump env .. for debuggin
for e in os.environ:
    print e, os.environ[e]

#load config.json
config_json=open("config.json").read()
config=json.loads(config_json)

products = []

for file in config["files"]:
    print file["filename"]
    print file["type"]
    #TODO..

#output products.json
with open('products.json', 'w') as out:
    json.dump(products, out)


