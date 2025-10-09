import sys
import os
import shutil
from copystatic import copy_files_recursive
from generate_page import generate_pages_recursive


dir_path_static = "./static"
dir_path_public = "./docs"


def main():
    basepath = ((sys.argv[1:]) and (sys.argv[1:][0])) or "/"
    print("Deleting docs directory...")
    if os.path.exists(dir_path_public):
        shutil.rmtree(dir_path_public)

    print("Copying static files to docs directory...")
    copy_files_recursive(dir_path_static, dir_path_public)

    #generate_page("content/index.md", "template.html", "public/index.html")
    generate_pages_recursive('content','template.html','docs', basepath)


main()