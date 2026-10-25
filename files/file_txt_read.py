# region 7.打开读取文件
import os  #导入operating system

my_file = '../data/myfile.txt'  #定义文件路径
my_file = os.path.join('../data', 'myfile.txt') #拼接文件路径 ⭐️

f = open(my_file) #打开文件
lines = f.readlines() #读取文件中所有行, readline每次只读取一行
for line in lines:
    print(line)
f.close() #关闭文件
# endregion
print('\n' + '-' * 80)
# region 7.2.另一种写法⭐️更推荐
#打开文档并读取‘r’是读取的意思；用‘with’可以自动关闭文件
with open(my_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')
# endregion

# region 7.3.Relative Path vs. Absolute Path（相对路径与绝对路径）
my_file = os.path.join('../data', 'myfile.txt') #relative path 相对路径
my_file = r'/'  #absolute path 绝对路径
# endregion

# region 7.4.查看/返回工作目录
cwd = os.getcwd()  # 获取当前工作目录 Get the current working directory
print(cwd)
my_file = os.path.join('../..', 'data', 'myfile.txt') #.：当前目录。..：上一级目录。
# endregion



