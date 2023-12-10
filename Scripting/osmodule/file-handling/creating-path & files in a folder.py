## Shell script 

# for i in {1..5}; do
#     touch "log_file_$i.log"
# done

# This program is creating a folder and files inside that folder

import os

print(f"Printing the CWD: \n{os.getcwd()} \n")

#myFile = os.open("text.txt", os.O_CREAT)
logfile_path = 'logfiles'
if not os.path.exists(logfile_path):
    os.mkdir(logfile_path)

os.chdir(logfile_path)

if not os.listdir():
    for i in range(1,6):
        filename = f"log-file-{i}.log"
        os.open(filename, os.O_CREAT)

print(os.listdir())


