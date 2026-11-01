"""
*  *  *  *  *
  *  *  *  *
    *  *  *
      *  *
        *

n = 5 - number of rows

compute how many bowls we need given n
"""
# region solution1. for loop
def compute_bowls(n):
    total = 0  # Initialize the total 初始化总数
    for i in range(1, n + 1):
        total = total + i
    return total
n=5
print(f'compute_boals: {compute_bowls(n)}')
# endregion

# region solution2. while loop
def count_bowls(n):  # Define a function 定义计算碗数量的函数
    i = 1  # Initialize the counter 初始化计数器
    bowls = 0  # Initialize the total number of bowls 初始化碗的总数

    while i <= n:  # Repeat while i is less than or equal to n 当i小于等于n时继续循环
        bowls = bowls + i  # Add i to bowls 将i累加到bowls
        i = i + 1  # Increase i by 1 每次循环将i增加1
    else:
        return bowls  # Return the total when the loop ends 循环正常结束后返回总数

n = 5
print(f'count_bowls({n})={count_bowls(5)}')
# endregion

# region recurse 递归  --- 报错
def count_bowls_recurse(n):  # Define a recursive function 定义递归函数
    if n == 1:  # Check the stopping condition 检查递归停止条件
        return 1  # Return 1 and stop recursion 返回1并停止递归
    else:
        return n + count_bowls_recurse(n - 1)  # Call the function itself with n-1 用n-1再次调用自身

result = count_bowls_recurse(5)  # Call the function with n=5 传入5调用函数
print(result)

n = 5
print(f'count_bowls({n})={count_bowls(5)}')
print(f'count_pins({n})={count_pins(5)}')
# endregion

# 测试哪个solution运行速度更快
from time import time  # Import the time function 导入时间函数

def time_func(func, n):  # Define a function to measure execution time 定义测量函数运行时间的函数
    print(f'Running {func.__name__} for n={n}')

    t0 = time()  # Record the start time 记录开始时间
    res = func(n)  # Execute the given function 执行传入的函数
    t1 = time()  # Record the end time 记录结束时间

    elapsed_time = t1 - t0  # Calculate elapsed time 计算运行耗时

    print(f'Result: {res}')  # Display the result 显示计算结果
    print(f'Elapsed time: {elapsed_time}')  # Display execution time 显示运行耗时

    time_func(count_bowls, n)  # Measure the for/while function's runtime 测量循环函数的运行时间
    time_func(count_pins, n)  # Measure the count_pins function's runtime 测量count_pins函数的运行时间
    time_func(count_bowls_recurse, n)  # Measure recursive function runtime 测量递归函数的运行时间
    time_func(count_bowls_sequence, n)  # Measure sequence function runtime 测量数学公式函数的运行时间
