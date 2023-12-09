import os 

# os.name - to get the name of the OS you are running the command.

print(f"The Os name is: {os.name}")

#  os.environ, os.getenv() and os.putenv() - The os.environ value is known as a mapping object that returns a dictionary of the user’s environmental variables. You may not know this, but every time you use your computer, some environment variables are set. These can give you valuable information, such as number of processors, type of CPU, the computer name, etc.

print(f"printing OS envs: {os.environ} \n")

print(f"Getting OS envs value: {os.getenv('USER')} \n")

# os.chdir() and os.getcwd()

print(f"Print the current working directory: {os.getcwd()} \n")
# print(f"change the workding directory: {os.chdir(r'/Users/divyanshusahu/Downloads/')} \n")  # output will be none onlt r' -- signifies raw string

print(f"Print the current working directory: {os.getcwd()} \n")

# os.mkdir() and os.makedirs() -- os.mkdir() allows us to create a single folder. os.makedirs() function will create all the intermediate folders in a path if they don’t already exist. Basically this means that you can created a path that has nested folders in it. I find myself doing this a lot when I create a log file that is in a dated folder structure, like Year/Month/Day. Let’s look at an example:


#os.mkdir('Test1') # will make folder in cwd it is making in downloads folder as we changed the directory in above command
path = r'/Users/divyanshusahu/Downloads/Github/python-code-practise/Scripting/Test3'
os.mkdir(path)

os.makedirs('Test/testnested')  # This will just make directory single or multiple but not files in the directory

