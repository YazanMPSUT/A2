import os, hashlib

files = os.listdir()
for file in files:
    with open("your_filename.png", "rb") as f:
        file_hash = hashlib.md5()
        while chunk := f.read(8192):
            file_hash.update(chunk)