import os
import os

if not os.path.exists('.env'):
    print("A .env file should exists with content: PERSONAL_TOKEN")
    os._exit(1)

with open('.env') as env_file:
    contents = env_file.readlines()
    print(contents)