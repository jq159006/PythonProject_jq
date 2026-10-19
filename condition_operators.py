#--------------------------------condition operators-------------
s = 'absef'
match s: #检查 s 的值是什么。类似于 if，用于多种情况的判断。
    case 'abcd':
        print('s is abcd') #如果 s == 'abcd'，就输出 s is abcd。
    case 'ab':
        print('s is ab')
    case _:
        print('s is not ab or abcd')

#----------------------loops---------------------------------------------
#for : 循环loop; i:每次循环的变量； range（10）- 生成0-9数字
for i in range(10):
    print(i)
print('-'*80) #输出80个 -，作为分隔线。

# reversed()： 把顺序反过来。起始值20，结束值50（不包含50）；步长3
for i in reversed(range(20,50,3)):
    print(i, end=' ')
print('\n' + '-'*80) #先换行，再输出80个分割线

i = 0
# while：当条件成立时，重复执行循环。
while i < 10: #这里表示只要 i < 10，就继续循环。
    print(i, end=' ')
    i = i + 2 #每次循环让 i 增加 2。
print('\n' + '-' * 80)

i = 0
# while：当条件成立时，重复执行循环。
while i < 10: #这里表示只要 i < 10，就继续循环。
    i += 1 #每次循环 i 增加 1。的另一种写法
    if i % 3 == 0: #%：取余数（Modulo）。判断 i 能否被 3 整除。
        continue #跳过本次循环剩余代码，直接进入下一次循环。
    print(i, end=' ')
print('\n' + '-' * 80)

for i in range(50, 20, -2):
    if i == 24:
        break #立即结束整个循环。当 i = 24 时，直接退出循环，不再执行下面的 print(i)。
    print(i, end=' ')
print('\n' + '-' * 80)

print('While loop')
###这里缺一个代码
print('\n' + '-' * 80)
#-------------------------------list------------------------
arr_a = [3, 5, 7, 9, 5, 9] #创建列表（List），依次输出所有元素，包括重复数字。
for i in arr_a:
    print(i, end=' ')

print('\n' + '-' * 80)
print('sets')
set_a = set(arr_a) #set()将列表转换成集合，自动去除重复元素。

for i in set_a:
    print(i, end=' ')
print('\n' + '-' * 80)

#set 不支持索引，要转回list
arr_a = [3, 5, 7, 9, 5, 9]
print(arr_a[2])

print('\n' + '-' * 80)
print('sets')
set_a = set(arr_a)

# print(set_a[2]) - can't be done - Set 不支持索引（Indexing），不能通过 [2] 访问元素。

for i in set_a:
    print(i, end=' ')

print('\n' + '-' * 80)
list_a = list(set_a)
print(list_a)
print(list_a[2])
print('\n' + '-' * 80)
#------------在set中添加或减少元素（缺代码）-------------------
list_a.append(8) #append()： 在列表（List）的末尾添加一个新元素 8。
print(list_a)

print('\n' + '-' * 80)
t_1 = (2, 56, 86)
print(t_1)
t_1.insert(2, 100)