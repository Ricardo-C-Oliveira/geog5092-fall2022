import os

with open('.env') as env_file:
    contents = env_file.readlines()
    print(contents)