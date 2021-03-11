import os
import logging

#TODO Set logger

PATH = "nil"

def set_path(PTH):
    #Log path
    PATH = PTH

#Path verification
def set_path(file_name):
    if PATH == 'nil':
        raise EnvironmentError("No path were specified")
    else:
        if not (PATH[-1] == "/" or PATH[-1] == "\\"):
            PATH += os.sep #Add separator if missing
        PATH += file_name

def write_file(file_name = "file", overwrite = True, data):
    set_path(file_name)
    #Get dict
    if not type(data) == dict:
        raise TypeError("Argument: \"data\" must be dictionary type.\nwrite_file(\"file_name\", \"overwrite\" = True, \"data\" = { }")
    else:
        pass

def read_file(file_name = "file"):
    set_path(file_name)
