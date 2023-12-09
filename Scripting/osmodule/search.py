import os

for dirpath,dirname,filename in os.walk('/Users/divyanshusahu/Downloads/Python/osmodule'):
    print(dirpath)
    print(dirname)
    print(filename)
    print(os.path.join(dirpath,*filename))


