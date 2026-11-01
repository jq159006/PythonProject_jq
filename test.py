import os
my_folder = 'data'  # Define the target folder 定义目标文件夹
my_files = os.listdir(my_folder)  # List folder contents 列出文件夹中的内容
for file in my_files:
    print(file)
fsize = os.path.getsize('../data')
print(fsize)
