
import shutil
import os
from posix import mkdir
from markdowntotext import *

def clear_copy(clear_path, copy_path):
    if os.path.exists(clear_path):
       shutil.rmtree(clear_path)
    os.mkdir(clear_path)
    path=os.listdir(copy_path)
    for p in path:
        x=os.path.join(copy_path,p)
        if os.path.isdir(x):
            os.mkdir(os.path.join(clear_path,p))
            clear_copy(os.path.join(clear_path,p),x)
        else:
            shutil.copy(x,os.path.join(clear_path,p))
    return


def generate_page(from_path, template_path, dest_path, basepath):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(template_path) as f:
        text_temp = f.read()
    with open(from_path) as x:
        text_from=x.read()
    content=markdown_to_html_node(text_from)
    html=content.to_html()
    title=extract_title(text_from)
    text_temp=text_temp.replace("{{ Title }}",title)
    text_temp=text_temp.replace("{{ Content }}",html)
    text_temp=text_temp.replace('href="/',f'href="{basepath}')
    text_temp=text_temp.replace('src="/' ,f'src="{basepath}')
    destpath=os.path.dirname(dest_path)
    os.makedirs(destpath, exist_ok=True)
    with open(dest_path,"w") as new:
        new.write(text_temp)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    content_path=os.listdir(dir_path_content)
    print(content_path)
    for dest in content_path:
        x=os.path.join(dir_path_content,dest)
        if os.path.isfile(x):
            y=os.path.join(dest_dir_path,(dest[:-2]+"html"))
            generate_page(x,template_path, y, basepath)
        else:
            y=os.path.join(dest_dir_path,dest)
            generate_pages_recursive(x,template_path, y, basepath)
    return
