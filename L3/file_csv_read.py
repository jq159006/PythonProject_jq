# read CSV → List → spilt → float、str → Dictionary → Calculation
import os

my_rates = os.path.join('data', 'rates.csv')
rates_dict = {}  # Create an empty dictionary 创建空字典,放在for循环外面

with open(my_rates, 'r') as r:
    lines = r.readlines()
    for line in lines[1:]: # Skip the header row 跳过表头
        parts = line.split(',')  # Split the string by comma 按逗号拆分字符串
        currency = parts[0]  # Extract the currency 提取货币名称
        value = float(parts[1])  # Convert the value to float 将汇率转换为浮点数

        rates_dict[currency] = value  # Add a key-value pair 添加键值对,一定要缩进到循环里
print(rates_dict)

amt_USD = 50  # Define the amount in USD 定义美元金额
amt_PLN = amt_USD * rates_dict['PLN']  # Convert
print(amt_PLN)