import os
import logging
import json

#TODO Set logger

PATH = "nil"

def set_path(PTH: str):
    #Log path
    PATH = PTH
    if not os._exists(PATH):
        os.mkdir(PATH)

#Path verification
def gen_path(file_name):
    if PATH == 'nil':
        raise EnvironmentError("No path were specified")
    else:
        if not (PATH[-1] == "/" or PATH[-1] == "\\"):
            PATH += os.sep #Add separator if missing
        return PATH + file_name

def write_file(file_name: str, data: dict):
    path = gen_path(file_name)
    #Get dict
    if not type(data) == dict:
        raise TypeError("Argument: \"data\" must be dictionary type.\nwrite_file(\"file_name\", \"overwrite\" = True, \"data\" = { }")
    elif data.__len__ == 0:
        raise ValueError("\"data\" must not be empty, for erasing data use clear() instead")
    else:
        jstream = open(path, "w+")
        json.dump(data, jstream, False)

        jstream.write()
        jstream.close()

def read_file(file_name = "file"):
    path = gen_path(file_name)
    if not os._exists(PATH):
        raise FileNotFoundError(f"File: {PATH} doesn't exists")
    else:
        jstream = open(path, "r")
        json.load(jstream)

        data = jstream.read()
        jstream.close()

        return data

#file_name = Name of the file, data = tuple to filter, returns a tuple
def get_data(file_name: str, data: tuple):
    DATA = read_file(file_name)
    if data.count == 0:
        return tuple(DATA.values())
    else:
        lData = list()
        for x in data:
            lData.append(DATA[x])
        return tuple(lData)

def update_file(file_name: str, data: dict):
    if file_name == "":
        raise ValueError("\"file_name\" must not be empty")
    elif data.__len__() == 0:
        raise ValueError("\"data\" must contain data to update")
    else:
        DATA = read_file(file_name)
        keys = tuple(data.keys())
        for x in keys:
            DATA[x] = data[x]
        write_file(file_name, DATA)