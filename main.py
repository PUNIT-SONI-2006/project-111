import os 
import shutil
from_dir='D:/Downloads'
to_dir='D:/Whitehatjr/class 111/project'
list_of_files=os.listdir(from_dir)
print(list_of_files)
for filename in list_of_files:
    name,extension=os.path.splitext(filename)
    print("Name of the file is:",name)
    print("Extension of the file is:",extension)
