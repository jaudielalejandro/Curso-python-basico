import os

def find(path, dir_name):
    found_paths = []
    for root, dirs, files in os.walk(path):
        if dir_name in dirs:
            found_paths.append(os.path.abspath(os.path.join(root, dir_name)))
    
    for path in found_paths:
        print(path)

# Ejemplo de uso
find("./tree", "python")
