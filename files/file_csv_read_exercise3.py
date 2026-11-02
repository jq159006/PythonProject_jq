# region 1. homework L3
# read CSV → List → spilt → float、str → Dictionary → Calculation
import os

my_rates = os.path.join('data', 'rates.csv')
rates_dict = {}  # Create an empty dictionary 创建空字典,放在for循环外面

with open(my_rates, 'r') as r:
    lines = r.readlines()
    for line in lines[1:]: # [1:]Skip the header row 跳过表头
        parts = line.strip().split(',')  # strip() 主要处理末尾的 \n；而 split(',') 才负责按照逗号分开内容。
        currency = parts[0]  # Extract the currency 提取货币名称
        value = float(parts[1])  # Convert the value to float 将汇率转换为浮点数

        rates_dict[currency] = value  # Add a key-value pair 添加键值对,一定要缩进到循环里
print(rates_dict)

amt_USD = 50
amt_PLN = amt_USD * rates_dict['PLN']  # Convert
print(amt_PLN)
# endregion

# region 2.使用library-pandas方法（更简洁）
import pandas as pd

df = pd.read_csv(my_rates)  # Read CSV into a DataFrame 读取CSV文件并转换为DataFrame
print(df.head())  # Display the first 5 rows 显示前5行

df_cur = df.set_index('Currency')  # Set Currency as the index 将Currency列设置为索引
print(df_cur['Value'])  # Select the Value column 提取Value列

rates = df_cur['Value'].to_dict()  # Convert Series to Dictionary 将Series转换为字典
print(rates)

print(rates['PLN'] * rates['EUR'])  # Multiply two dictionary values 将字典中两个值相乘
# endregion

