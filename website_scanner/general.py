import os

def create_directory(name):
    if not os.path.exists(name):
        os.makedirs(name)
    else:
        print("Directory already exists, moving on ...")

def create_file(path, data):
    new_file = open(path, "w")
    new_file.write(data)
    new_file.close()
