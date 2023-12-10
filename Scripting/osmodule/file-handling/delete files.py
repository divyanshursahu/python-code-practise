import os

path = os.getcwd()

for roots, dirs, files in os.walk(path):
    #print(roots)
    #print(dirs)
    for file in files:
        if file.endswith('.log'):
            file_path = os.path.join(roots,file)
            os.remove(file_path)
            print(f"deleted {file_path}")
           # print(roots)
            # print(file)
 #   < ---- check below code --->
    for dir in dirs:
        #print(dir)
        dirpath = os.path.join(roots,dir)
        for file in files:
            if not os.path.exists(file):
        #print(dirpath)
                os.rmdir(dirpath)
            else:
                print(f"{dir} not empty")
    
        