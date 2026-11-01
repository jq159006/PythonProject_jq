def sum_it(a: int, b: int) -> int:  # Define parameter and return type hints 定义参数及返回值的类型提示
    return a + b

print(sum_it(1.67, 32.53)) #虽然设置了整数，但是小数仍然可以运行


def sum_it_params(a: int = 5, b: int = 10):  # Set default parameter values 设置参数默认值
    s_i = 35254
    return a + b

print(sum_it_params(1.67))
print(sum_it_params())
print(sum_it_params(b=15))

print('-' * 60)


b = 4
d = 0

if b > 5:
    d = 10
else:
    d = 5

print(f'd={d}')  # Print d using an f-string 使用f-string输出d


for i in range(10):
    bi = i * 10

print(f'bi={bi}')

res = sum_it_params(5, 10)  # Pass two arguments to the function 向函数传入两个参数
print(f'res={res}')

# print(f's_i={s_i}')  # Access a local variable outside the function 在函数外访问局部变量（会报错）