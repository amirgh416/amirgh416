import os
  
all_files = list()
all_dirs = list()
  
for root, dirs, files in os.walk("root/home/project"):
    all_files.extend(files)
    
    all_dirs.extend(dirs)
  
print(all_files)
print(all_dirs)