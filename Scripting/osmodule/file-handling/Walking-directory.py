import os

path = os.getcwd()
for root, dirs, files in os.walk(path):
    print(root)
    for dir in dirs:
        print(dir)
    for file in files:
        print(os.path.join(root,file))
        
            #os.remove('*.log')