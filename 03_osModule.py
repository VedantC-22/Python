import os

# specifying the directory, we can enter string also
path = os.getcwd();
print(f"Current directory: {path}")

# list of all files available in specified path
for items in os.listdir(path):
    print(items)