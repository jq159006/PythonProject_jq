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

