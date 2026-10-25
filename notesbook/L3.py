#region 1. condition operators
from os import remove

s = 'absef'
match s: #检查 s 的值是什么。类似于 if，用于多种情况的判断。
        # match（case）更适合匹配某个值。if(else)更适合比较条件比如比大小
    case 'abcd':
        print('s is abcd') #如果 s == 'abcd'，就输出 s is abcd。
    case 'ab':
        print('s is ab')
    case _:
        print('s is not ab or abcd')
# endregion


#region 2. loops
#1) for : 循环loop; i:每次循环的变量； range（10）- 生成0-9数字
for i in range(10):
    print(i)
print('-'*80) #输出80个 -，作为分隔线。
# 1.1
for i in range(5,11):
    print(i)
print('-'*80)
# 1.2
for i in range(50, 20, -2): #（步长，每次减2）
    if i == 24:
        break #立即结束整个循环。当 i = 24 时，直接退出循环，不再执行下面的 print(i)。
    print(i, end=' ')
print('\n' + '-' * 80)

#2) reversed()： 把顺序反过来。起始值20，结束值50（不包含50）；步长3
for i in reversed(range(20,50,3)):
    print(i, end=' ')
print('\n' + '-'*80) #先换行，再输出80个分割线

#3) while：当条件成立时，重复执行循环。
i = 0
while i < 10: #这里表示只要 i < 10，就继续循环。
    print(i, end=' ')
    i = i + 2 #每次循环让 i 增加 2。(也可以写成 i+= 2)
print('\n' + '-' * 80)

#3.1) while：当条件成立时，重复执行循环。
i = 0
while i < 10: #这里表示只要 i < 10，就继续循环。
    i += 1 #每次循环 i 增加 1。的另一种写法
    if i % 3 == 0: #%：取余数（Modulo）。判断 i 能否被 3 整除。
        continue #如果能被3整除则跳过print，返回循环
    print(i, end=' ')#不能被3整除的，输出i,然后返回循环
print('\n' + '-' * 80)
#3.2
i = 0
while i < 10: #这里表示只要 i < 10，就继续循环。
    i += 1 #每次循环 i 增加 1。的另一种写法
    if i % 3 == 0: #%：取余数（Modulo）。判断 i 能否被 3 整除。
        continue #如果能被3整除则跳过print，返回循环
    if i == 8:
        break #当i=8时，立即结束整个循环
    print(i, end=' ')#不能被3整除的，输出i,然后返回循环
print('\n' + '-' * 80)
# endregion


# region 3. list_sets_tuple_dicts
#创建列表（List），依次输出所有元素，包括重复数字。⭐️
arr_a = [3, 5, 7, 9, 5, 9]
for i in arr_a:
    print(i, end=' ')
print('\n' + '-' * 80)

#set()将list(列表)转换成set（集合），set不允许元素重复⭐️。是无序集合，不保证顺序
print('sets')
set_a = set(arr_a)
for i in set_a:
    print(i, end=' ')
print('\n' + '-' * 80)

#set 不支持索引，要转回list
arr_a = [3, 5, 7, 9, 5, 9]
print(arr_a[2])
print('\n' + '-' * 80)

# print(set_a[2]) - can't be done - Set 不支持索引（Indexing）⭐️，不能通过 [2] 访问元素。
#set + for loop
set_a = set(arr_a)
for i in set_a:
    print(i, end=' ')
print('\n' + '-' * 80)

# set 转为 list
list_a = list(set_a)
print(list_a)
print(list_a[2])
print('\n' + '-' * 80)

# 在set中添加或减少元素（缺代码）
list_a.append(8) #append()： 在列表（List）的末尾添加一个新元素8。
print(list_a)
list_a.insert(2, 100) #在第3位置处，插入数字‘100’
print(list_a)
print(type(list_a))
print('\n' + '-' * 80)

#remove & pop 移除数字
arr_a = [3, 5, 7, 9, 5, 9]
list_a = list(arr_a)
print(list_a)
list_a.remove(5) # 直接移除数字,按顺序移除第一个‘5’
print(list_a)

list_a.pop(1) #根据位置移除数字
print(list_a)
# endregion

#region 4. list[]列表 VS tuple()元组。
# 共同点：都有序，都允许重复；都支持索引
# 不同点：tuple 不可以修改元素；添加元素；和append（）
t_1 = (2,56,86)
print(t_1)
print(type(t_1))
# endregion

#region 5. 2D lists-二维列表
points = [[1, 2], [4, 5], [7, 8]]
print(points)
el_5 = points[1][1] # 第2个框的第2位数字
print(el_5)
print(type(points))
print(type(points[2]))

for r in points:
    print(r)
    for c in r:
        print(c)
print('\n' + '-' * 80)
#-----------3x3--------------
points = [[1, 2, 5],
          [4, 5, 4],
          [7, 8, 8]]

print(points)
el_5 = points[1][1]
print(el_5)
print(type(points))
print(type(points[2]))

for r in points:
    print(r)
    for c in r:
        print(c)
print('\n' + '-' * 80)
# endregion

#region 2D lists-exercise-nested loops
points = [[1, 2, 5],
          [4, 5, 4],
          [7, 8, 8]]
#sum_rows：先取一行r，再把这一行加起来c。
def sum_rows(my_list):
    result = [] #创建空列表，准备保存每行的结果。
    for r in my_list: #：每次从 my_list 中取出一个子列表，放进变量 r。
        total = 0 #很重要！准备开始计算当前这一行的总和，先从0开始。为了每一行能够做到单独求和
        for c in r: #从当前这一行 r 中，每次取出一个数字，放进变量 c。
            total = total + c
        result.append(total)
    return result
print(sum_rows(points))

#按列相加：先确定要计算哪一列，再从每一行中取出这一列的数字相加。
def sum_cols(my_list):
    result = []
    for i in range(len(my_list[0])): #i - （0,1,2）
        total = 0
        for r in my_list: #my list 还是行，但是r[i]提取出来的是正好是每一列的值。比如i=0,就是第一行提取第一个数+循环跳转到第二行提取第一个数依次类推
            total = total + r[i]
        result.append(total)
    return result
print(sum_cols(points))

#整个相加
def sum_list(my_list):
    total = 0
    for r in my_list: #外层循环：每次取出一整行。
        for c in r: #内层循环：从当前这一行中逐个取数字。
            total = total + c
    return total
print(sum_list(points))
# endregion

# region 6.dictionary-字典
# 1）dictionary 允许我们通过key直接找到对应的value[()]
rates_list = [('USD', 3.8), ('PLN', 1), ('EUR', 4.3)]
rates_dict = dict(rates_list)
print(rates_dict)
print(rates_dict['USD'])
# 6.1）直接创建dictionary，比1）要更方便，用{}
rates_dict = {'USD': 3.8, 'PLN': 1, 'EUR': 4.3}
print(rates_dict)
for key, value in rates_dict.items(): #遍历 Dictionary，每次同时取出一个 Key和对应的 Value。
    print(key, value)#表达方式1
# 6.2表达方式2
for key in rates_dict.keys():
    print(key, rates_dict[key])

print(type(rates_dict.keys()))
print(set(rates_dict.keys()))
print(rates_dict.values())
print(type(rates_dict.values()))
print(list(rates_dict.values()))

#region 6.3关于报错[]与get
my_exch_rate = rates_dict['GBP'] #会报错
my_exch_rate = rates_dict.get('GBP') #.get与[]不同，在key不存在时不会报错
my_exch_rate = rates_dict.get('GBP',2.5) #Default Value（默认值），仅当 Key 不存在时使用
print(my_exch_rate)
# endregion

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

# region 8.writing a file⭐️
import os
my_file = os.path.join('../data', 'fileout.txt')

f = open(my_file, 'w')  # Open the file in write mode 以写入模式打开文件
f.write('Hello World\n')
f.write('Python here\n')
f.write('At SGH\n')
f.close()
# endregion

# region 8.2.Buffer & flush()（缓冲区）⭐️⭐️
# 文件真正写入存储系统前，数据临时停留的一个空间。执行 f.close() 后，内容才出现在文件中。
f = open(my_file, 'w')
f.write('First line\n')
f.write('Second line\n')
f.flush()  # Flush buffered data 刷新缓冲区中的数据
f.write('Third line\n')
f.close()
# endregion

# region 8.3.Append Mode（追加模式）
with open(my_file, 'a') as f:  # Open the file in append mode 以追加模式打开文件
    f.write('Another line\n')
# endregion

# region homework1
# endregion
# region homework2
# endregion




