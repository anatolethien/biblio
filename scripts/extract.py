#!/usr/bin/env env/Scripts/python

import os
import glob
import zipfile as zip

print('Removing current files...')

path = "assets/*.csv"
for f in glob.glob(path):
    os.remove(f)

print('Extracting...')

with zip.ZipFile("downloads/archive.zip", "r") as archive:
    archive.extractall("assets/")

print('Done!')
