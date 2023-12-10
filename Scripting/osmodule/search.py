import os

path ='/Users/divyanshusahu/Downloads/Github/python-code-practise/Scripting/osmodule/file-handling'
for dirpath,dirname,filename in os.walk(path):
    print(dirpath)
    print(dirname)
    print(filename)
    print(os.path.join(dirpath,*filename))


