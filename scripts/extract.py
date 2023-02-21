#!/usr/bin/env python3

import os
import glob
import zipfile as zip
import broom

def remove_previous():
    previous_path = 'downloads/*.csv'
    print("Removing current files...")
    for file in glob.glob(previous_path):
        os.remove(file)

def extract_archive():
    origin_path = 'downloads/archive.zip'
    destination_path = 'downloads/'
    print(f"Extracting to {destination_path}...")
    with zip.ZipFile(origin_path, 'r') as archive:
        archive.extractall(destination_path)

if __name__ == '__main__':
    print("Extract!")
    remove_previous()
    extract_archive()
    broom.books_broom()
    broom.authors_broom()
    broom.categories_broom()
    broom.formats_broom()
    print("Done!")

