import psutil

gb_converstion = 1024 ** 3
memory = psutil.virtual_memory()
print(f"Printing all the memory in the Machine: {memory}")

total_memory = memory.total / gb_converstion
print(f"Total memory in the machine: {total_memory}")

free_mem = memory.available / gb_converstion
print(f"The free mem in machine: {round(free_mem, 2)}")

used_mem = memory.used / gb_converstion
print(f"The current used memory of machine: {round(used_mem, 2)} ")

percent_used = memory.percent
print(f"The memory percentage used: {percent_used}")

#print(psutil.pids())
#process = psutil.process_iter()
process = psutil.Process()
print(process.memory_info().rss)