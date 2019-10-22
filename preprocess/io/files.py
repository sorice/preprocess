#!/usr/bin/env python 3.6

"""
Files includes functions to load multiple files to be processed.
"""

from typing import List
import os

def get_files(path :str, extension :str) -> List[str]:
    "Return a target list of files in a path based on its extensions."

    target_files = []

    if path == '':
        path = os.getcwd()
    
    for file in os.listdir(path):
        if file.endswith(extension):
            target_files.append(os.path.join(path,file))
    
    return target_files
