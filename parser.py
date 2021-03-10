import os
import logging

#TODO Set logger

PATH = "nil"

def set_path(PTH):
    #Log path
    PATH = PTH

#Path verification
def is_path():
    if PATH == 'nil':
        False
    else:
        True

def write_file(file_name = "file", overwrite = True, *data):
    if not is_path():
        raise EnvironmentError("No path were specified")
    else:
        if not (PATH[-1] == "/" or PATH[-1] == "\\"):
            PATH += os.sep #Add separator if missing
        PATH += file_name

def read_file(file_name = "file"):
    if not is_path():
        raise EnvironmentError("No path were specified")
    else:
        if not (PATH[-1] == "/" or PATH[-1] == "\\"):
            PATH += os.sep
        PATH += file_name
        