'c:\\spam\\eggs.png'
print('\\')
r'c:\spam\eggs.png'
print(r'c:\spam\eggs.png')

path = '\\'.join(['folder1', 'folder2', 'folder3', 'file.png'])



import os
path = os.path.join('folder1', 'folder2', 'folder3', 'file.png')
print(path)
print(os.getcwd())