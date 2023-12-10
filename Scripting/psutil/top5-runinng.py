import psutil
import os



def get_top_processes(num_processes=5):
    # Get a list of all running processes
    all_processes = psutil.process_iter(['pid', 'name', 'memory_info'])

    # Sort processes by memory usage
    sorted_processes = sorted(all_processes, key=lambda x: x.info['memory_info'].rss, reverse=True)

    # Print information for the top processes
    print(f"Top {num_processes} processes by memory usage:")
    for i, process in enumerate(sorted_processes[:num_processes], start=1):
        pid = process.info['pid']
        name = process.info['name']
        memory_usage = process.info['memory_info'].rss / (1024 ** 2)  # Convert to megabytes
        print(f"{i}. PID: {pid}, Name: {name}, Memory Usage: {memory_usage:.2f} MB")

# Get top 5 processes by memory usage
get_top_processes(5)


# import psutil
# from operator import itemgetter

# def get_top_processes(num_processes=5):
#     # Get a list of all running processes
#     all_processes = psutil.process_iter(['pid', 'name', 'memory_info'])

#     # Sort processes by memory usage
#     sorted_processes = sorted(all_processes, key=itemgetter('memory_info', 'rss'), reverse=True)

#     # Print information for the top processes
#     print(f"Top {num_processes} processes by memory usage:")
#     for i, process in enumerate(sorted_processes[:num_processes], start=1):
#         pid = process.info['pid']
#         name = process.info['name']
#         memory_usage = process.info['memory_info'].rss / (1024 ** 2)  # Convert to megabytes
#         print(f"{i}. PID: {pid}, Name: {name}, Memory Usage: {memory_usage:.2f} MB")

# # Get top 5 processes by memory usage
# get_top_processes(5)
