#region 1.CSV vs JSON
# CSV：适合保存规则的二维表格，例如货币与汇率。
# JSON：能够保存 List、Dictionary，以及它们组成的 Nested Structures（嵌套结构）。

import os
import json

my_json_file = os.path.join('..', 'data', 'rates.json')  # Create the file path 创建文件路径

with open(my_json_file) as f:  # Open the JSON file 打开JSON文件
    data = json.load(f)  # Load JSON data into Python 将JSON数据读取为Python对象
    rates_dict = data[0]  # Get the first dictionary 提取第一个字典
    weekdays_dict = data[1]  # Get the second dictionary 提取第二个字典

    print(rates_dict)
    print(rates_dict["USD"])  # Get the value for USD 获取USD对应的值
    print(type(rates_dict["USD"]))  # Check the value's data type 检查该值的数据类型
    print(weekdays_dict)