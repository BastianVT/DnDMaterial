import os

path = 'D:\\Dnd\\Future Project'

for file in os.listdir(path):
    if file.endswith('.md'):
        print(os.path.join(path, file))