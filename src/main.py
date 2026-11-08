import os
import shutil

from textnode import *


def main():
    copy_static()

def copy_static(path="public"):
    delete_public(path)
    copy()

def delete_public(path):
    if not os.path.exists(path):
        os.mkdir(path)
    for file in os.listdir(path):
        filepath = f"{path}/{file}"
        if os.path.isfile(filepath):
            os.remove(filepath)
        elif os.path.isdir(filepath):
            delete_public(filepath)
            os.rmdir(filepath)

def copy(path="static", dest="public"):
    for file in os.listdir(path):
        filepath = f"{path}/{file}"
        dest2 = f"{dest}/{file}"
        if os.path.isfile(filepath):
            shutil.copy(filepath, dest2)
        if os.path.isdir(filepath):
            os.mkdir(dest2)
            copy(filepath, dest2)



main()
