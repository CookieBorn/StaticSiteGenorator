import shutil
import os
from posix import mkdir

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
