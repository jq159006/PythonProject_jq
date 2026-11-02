import os
import json

rates_dict = {"USD": 3.8, "PLN": 1, "EUR": 4.3}  # Create a dictionary of exchange rates 创建汇率字典

weekdays_dict = {1: "Monday", 2: "Tuesday", 3: "Wednesday"}  # Create a dictionary of weekdays 创建星期字典

my_list = [rates_dict, weekdays_dict]  # Store two dictionaries in a list 将两个字典放入列表

my_json_file = os.path.join('..', 'data', 'rates.json')  # Define the JSON file path 定义JSON文件路径

with open(my_json_file, 'w') as f:  # Open the file in write mode 以写入模式打开文件
    json.dump(my_list, f)  # Save the list as JSON 将列表保存为JSON文件