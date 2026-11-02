"""
*  *  *  *  *
  *  *  *  *
    *  *  *
      *  *
        *

n = 5 - number of rows

compute how many bowls we need given n
"""
# region solution1. for loop - 根据指定的序列或范围循环
def compute_bowls(n):
    total = 0  # Initialize the total 初始化总数
    for i in range(1, n + 1):
        total = total + i
    return total
n=5
print(f'compute_boals: {compute_bowls(n)}')
# endregion

# region solution2. while loop - 只要条件成立就继续循环
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

# region solution3. recurse 递归  --- 报错
# recurse: 就是一个 Function 在自己内部再次调用自己。
def count_bowls_recurse(n):  # Define a recursive function 定义递归函数
    if n == 1:  # Check the stopping condition 检查停止条件
        return 1  # Return 1 for the first row 第一排只有1个球
    else:
        return n + count_bowls_recurse(n - 1)  # Add the current row to previous rows 当前排加上之前所有排的球数
print(count_bowls_recurse(5))  # Calculate for 5 rows 计算5排的总球数

# endregion

# region solution4. 数学方式
def count_bowls_sequence(n):
    return round((n * (n + 1)) / 2)
n=5
print(f'compute_boals: {compute_bowls(n)}')
# endregion

# 测试哪个solution运行速度更快
from time import time  # Import the time function 导入时间函数

def time_func(func, n):  #定义函数：执行指定func并计算运行了多少秒
    print(f'Running {func.__name__} for n={n}')

    t0 = time()  # Record the start time 记录开始时间
    res = func(n)  # Execute the given function 执行传入的函数
    t1 = time()  # Record the end time 记录结束时间

    elapsed_time = t1 - t0  # Calculate elapsed time 计算运行耗时

    print(f'Result: {res}')  # Display the result 显示计算结果
    print(f'Elapsed time: {elapsed_time}')  # Display execution time 显示运行耗时
    n = 998
    n = 50000000

    # print(f'count_bowls({n})={count_bowls(n)}')
    # print(f'count_pins({n})={count_pins(n)}')
    # print(f'count_bowls_recurse({n})={count_bowls_recurse(n)}')
    # print(f'count_bowls_sequence({n})={count_bowls_sequence(n)}')

    # time_func(round((n * (n + 1))/2), n)
    # time_func(count_bowls(n), n)
    time_func(count_bowls, n)
    time_func(count_pins, n)
    # time_func(count_bowls_recurse, n)
    time_func(count_bowls_sequence, n)