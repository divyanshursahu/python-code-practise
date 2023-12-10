import os

print(f"The CWD: \n{os.getcwd()}")
root_dir = os.getcwd()
dir_paths = ['dir1', 'dir2', 'dir3']
for path in dir_paths:
    if not os.path.exists(path):  # os.path.isdir can be also used to check if it is a directory and exists
        os.makedirs(path)    
    else:
        print(f"The {path} already exists")

for path in dir_paths:
    os.chdir(path)
    for file in path:
        if not os.path.exists(file):
            for i in range(0,6):
                os.open(f'test-{i}.log', os.O_CREAT)
               
    
    os.chdir(root_dir)
