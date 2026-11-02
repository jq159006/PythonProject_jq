#region 1. functions & parameter
def sum_it(a: int, b: int) -> int:
    return a + b

print(sum_it(1.67, 32.53)) #虽然不是整数，但依然可以运行

def sum_it_params(a=5, b=10): #如果没有说明ab的值，就默认a=5b=10
    s_i = 35252 #为了说明函数里面创建的 s_i，函数外部不能直接使用。
    summ = a +b
    # return summ, - adding a comma turns the output into a tuple with an empty second element
    return summ #return是把 summ 当前的值返回给函数调用者。无法带到外部

print(sum_it_params(1.67))
print(sum_it_params())
print(sum_it_params(b=15))
print('-'*60)
# endregion

#region 2.区分if/for/function
# 2.1 if
b = 4
d = 0
if b > 5:
    d = 10
else:
    d = 5
print(f'd={d}')
# 2.2 for
for i in range(10):
    bi = i * 10
print(f'bi={bi}') #循环结束后，bi 保留最后一次赋值的结果。
# 2.3 function
res = sum_it_params(5, 10)
print(f'res={res}') #函数内部的局部变量不是完全不能把值传出去，而是要通过 return 等方式明确传递。
#print(f's_i={s_i}') - 报错，因为function会创建自己的local scope（局部作用域）
# endregion

# region 3. nested function 嵌套函数
def sum_and_multiply(a, b):
    summ = a + b

    def multiply(a, b):
    #    print(a, b, c, d)
        b = 100
        return a* b
    #def multiply():
    #    return a * b
    #multi = multiply()
#    multi = multiply(191, 141)
    multi = multiply(a, b)
    return summ, multi

result = sum_and_multiply(5, 10)
print(f'result={result}')
print(f'type(result)={type(result)}')

sum_ab, multi_ab = sum_and_multiply(5, 10)
print(f'sum_ab={sum_ab}, multi_ab={multi_ab}')

#print(sum_and_multiply.multiply(1, 3))