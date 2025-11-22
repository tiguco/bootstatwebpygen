from textnode import TextNode, TextType
from dirutil import copy_directory_recursive
from pagegenerator import generate_pages_recursive
import sys



static_dir_path = "./static"
public_dir_path = "./docs"
content_dir_path = "./content"
template_path = "./template.html"
default_basepath = "/"


def main():

    basepath = default_basepath

    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    copy_directory_recursive(static_dir_path, public_dir_path)

    generate_pages_recursive(content_dir_path, template_path, public_dir_path, basepath)



main()
