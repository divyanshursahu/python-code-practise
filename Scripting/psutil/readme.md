## Documentation:

https://www.geeksforgeeks.org/psutil-module-in-python/

The `psutil` module in Python returns memory information in bytes. When you use the `psutil.virtual_memory()` function, it provides details about virtual memory, including total, available, and used memory, all in bytes.

If you want to convert these values to a more human-readable format, you can use factors such as kilobytes (KB), megabytes (MB), gigabytes (GB), etc. In the example I provided earlier, the conversion to gigabytes was done using the factor `1024 ** 3`.

Here's a breakdown of the units:

- Kilobyte (KB): `1024` bytes
- Megabyte (MB): `1024 ** 2` bytes
- Gigabyte (GB): `1024 ** 3` bytes
- Terabyte (TB): `1024 ** 4` bytes
- Petabyte (PB): `1024 ** 5` bytes

You can adjust the conversion factor based on your preference for the size unit you want to display. For example, if you want to display memory in megabytes, you would use `1024 ** 2` instead of `1024 ** 3`.