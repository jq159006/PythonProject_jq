import sys

print('hello world')

# end - 不换行输出
print('2nd line', end=' ')
print('continue 2nd line')

# 1）字符串格式化
a=35
b=35
c=a+b
print(c)
print(f'{a}')
print(f'{b}')
print(f'{c}')
# type
type_c = type(c)
print(type_c) # 如果只输入这个，就只会显示类别
print(f'type_c: {type(c)}') # f'变量名：{表达式}'
print(f'type_c: {type(c)} c= {c}') # f'变量名：{表达式} c ={数值}'.反正就是所有要输出的都放在f''内，然后用{}
# 2）格式化字符串的方式
d = 4161619559743735214926379646432749649142749646472546919642476461
e = 5659228963731945742691643461942541966212415748411698769986258256
f = d + e
print(f'f={f}')
print(f'type_f = {type(f)}')
print('f={}'.format(f)) #"{}".format(value),

# 看有多少位数字
s_d = str(d)
num_digits_d = len(s_d)
print(f'num_digits_d={num_digits_d}')

# float example
f_d = 4161619559743735214926379646432749649142749646472546919642476461.0
f_e = 5659228963731945742691643461942541966212415748411698769986258256.0
print(f'f_d={f_d}')
print(f'f_e={f_e}')
print(f'type(f_d)={type(f_d)}')
print(f'type(f_e)={type(f_e)}')
f_f = f_d + f_e
print(f'f_f={f_f}')

# 科学计数法 e 表示“乘以 10 的多少次方”。
# 1.52e-2 =1.52×10^-2= 1.52×0.01
g = 1.52e-2
print(f'g={g}')

# 浮点数的极限与溢出，当超出极限时，就会得到inf（infinity，无穷大），不会报错
max_f = 1.8e308 #1.8*10^308
print(f'max_f={max_f}')

print(sys.float_info) #查询浮点数的信息

# 二进制 binary system
b_b = 0b1011
print(f'b_b={b_b}')
# 十六进制 hexadecimal
h_c = 0x1f
print(f'h_c={h_c}')

# round() 保留小数
a = 1.9835
b = round(a,2)
print(f'a={a}')
print(f'b={b}')
# `%` 取余数 -  `r = ? % 4` 表示除法余数
f = 10
g = 4
r = f % g
print(f'r = {r}')

# list列表、数组
arr_a = [3, 5, 7, 9]
print(f'arr_a = {arr_a}')
print(f'3rd elem = {arr_a[2]}')

arr_b = [3, '5', 7.0, 9] #列表里可以是任何type
print(f'arr_b = {arr_b}')

for e in arr_b:
    print(f'e={e}, type_e={type(e)}') #a loop

#s[start:end]` 取子串/子数组
s_1 = 'abcdefg'
s_2 = 'hijkl'
print(f's_1[2] = {s_1[2]}') # c - 3
print(f's_1[2:4] = {s_1[2:4]}') #cd - [3,5)
print(f's_1[:4] = {s_1[:4]}') #第5个之前的 <5
print(f's_1[4:] = {s_1[4:]}') #第5个及以后的 ≥5
print(f's_1[-3:] = {s_1[-3:]}')  # 最后3个字符 the last three elements
print(f's_2[-1:] = {s_1[-1:]}') #最后一个字符
#合并 aggregation
s_3 = s_1 + s_2
print(f's_3 = {s_3}')

# 换行\n
print('\nabgg\ngrhren')
print(r'\nabgg\ngrhren') #r 代表 raw string，意思是“原始字符串”

# ord()：把字符转换成对应的数字编码. 根据ASCII代码表
c_a = ord('a')
print(f'c_a = {c_a}')
# chr()：把数字编码转换成对应的字符。根据ASCII代码表
c_b = chr(98)
print(f'c_b = {c_b}')

s_5 = 'abcdefgabcdefg'
i_abc = s_5.find('bc') #find 从左往右找第一个
print(f'i_abc = {i_abc}')
i_abc = s_5.rfind('bc') #rfind 从右往左找最后一个
print(f'i_abc = {i_abc}')
# index 和 find 类似，但找不到会报错
i_abc = s_5.index('bc')
print(f'i_abc = {i_abc}')
i_abc = s_5.rindex('bc')
print(f'i_abc = {i_abc}')

#字符串的 split() ：按指定分隔符把字符串拆成一个列表。
s_6 = '1445;2553;3647'
arr_s6 = s_6.split(';')
print(f'arr_s6 = {arr_s6}')

s_7 = '    sgsbg  '
s_8 = s_7.split()
print(f's_8 = {s_8}')

# 初始化布尔bool变量
p = True
q = False
print(f'type_pq: {type(p)}')

if p:
    print('p is True')  # 因为 p 是 True，所以执行这一行
else:
    print('p is False') # 否则执行这一行

print('----------------------------')
# and -- p 是 True，q 是 False，p and q 的结果是 False，所以不会执行这一行
if p and q:
    print('p and q is True')
else:
    print('p or q is False')

print('----------------------------')

#or -- p 是 True，q 是 False，p or q 的结果是 True
if p or q:
    print('p or q is True')  # 条件成立，执行这一行
else:
    print('p and q is False')
