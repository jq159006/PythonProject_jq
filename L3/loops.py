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


