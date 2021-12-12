import subprocess
import zipfile
import os
import pathlib

file_dir = pathlib.Path(__file__).parent.resolve()

subprocess.run('wget https://www.idrivedownloads.com/downloads/linux/download-for-linux'
               '/IDrive_Scripts/IDriveForLinux.zip'.split())
with zipfile.ZipFile('IDriveForLinux.zip', 'r') as zip_ref:
    zip_ref.extractall(file_dir)
