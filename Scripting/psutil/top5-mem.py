import psutil
import os

#all_processes = psutil.process_iter(['pid', 'name', 'memory_info', 'username', 'cwd'])
all_processes = psutil.process_iter(['pid', 'name', 'memory_info'])
print(all_processes)
for proc in all_processes:
    print(proc.info)



# for proc in psutil.process_iter(['pid', 'name', 'username']):
#     print(proc)