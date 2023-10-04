import os

path = os.getcwd()
print("Current Directory", path)
 
# prints parent directory
print(os.path.abspath(os.path.join(path, os.pardir)))
####
# get current directory
path = os.getcwd()
print("Current Directory", path)
print()
 
# parent directory
parent = os.path.dirname(path)
print("Parent directory", os.path.basename(parent))

