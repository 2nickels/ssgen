import os
import shutil
import sys

from markdown_to_html_node import markdown_to_html_node
from textnode import *

dir_path_static = "./static"
dir_path_public = "./docs"
dir_path_content = "./content"
template_path = "./template.html"
if len(sys.argv) > 1:
    basepath = sys.argv[1]
else:
    basepath = "/"

def main():
    print(basepath)
    copy_static()
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)

def copy_static(path="./docs"):
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

def copy(path="./static", dest="./docs"):
    for file in os.listdir(path):
        filepath = f"{path}/{file}"
        dest2 = f"{dest}/{file}"
        if os.path.isfile(filepath):
            shutil.copy(filepath, dest2)
        if os.path.isdir(filepath):
            os.mkdir(dest2)
            copy(filepath, dest2)

def extract_title(markdown) -> str:
    mdsplit = markdown.split("\n\n")
    for line in mdsplit:
        if line.startswith("# "):
            line = line.strip("# ").rstrip()
            return line
    raise ValueError("Invalid: No title found")

def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page {from_path} to {dest_path} using {template_path}")
    with open(from_path) as fpath:
        index = fpath.read()
    with open(template_path) as tpath:
        template = tpath.read()
    html = markdown_to_html_node(index).to_html()
    title = extract_title(index)
    temp = template.replace(r"{{ Title }}", title).replace(r"{{ Content }}", html).replace('href="/', f'href="{basepath}').replace('src="/', f'src="{basepath}')
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)
    with open(dest_path, "w") as file:
        file.write(temp)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    dir = os.listdir(dir_path_content)
    for i in dir:
        if os.path.isfile(os.path.join(dir_path_content, i)):
            generate_page(os.path.join(dir_path_content, i), template_path, os.path.join(dest_dir_path, "index.html"), basepath)
        elif os.path.isdir(os.path.join(dir_path_content, i)):
            generate_pages_recursive(os.path.join(dir_path_content, i), template_path, os.path.join(dest_dir_path, i), basepath)



main()
