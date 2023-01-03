#!/usr/bin/env env/Scripts/python
import zipfile as zip

print('Extract!')

with zip.ZipFile("downloads/archive.zip", "r") as zip_ref:
    zip_ref.extractall("assets/")
