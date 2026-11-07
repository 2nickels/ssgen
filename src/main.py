import os
import shutil

from textnode import *


def main():
    copy_static()

def copy_static(path="public"):
    for file in os.listdir(path):
        os.remove(f"{path}/{file}")
    #if os.path.exists("public/"):
     #   shutil.rmtree("public")
    #os.mkdir("public")

main()
