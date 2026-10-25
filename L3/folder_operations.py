import os

my_folder = os.path.join('..','data')
my_files = os.listdir(my_folder)  # List folder contents 列出文件夹中的内容
print(my_files)
fsize = os.path.getsize('../data/myfile.txt')
print(fsize)
