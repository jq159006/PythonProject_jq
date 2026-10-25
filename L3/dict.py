# region dictionary-字典
# 1）dictionary 允许我们通过key直接找到对应的value[()]
rates_list = [('USD', 3.8), ('PLN', 1), ('EUR', 4.3)]
rates_dict = dict(rates_list)
print(rates_dict)
print(rates_dict['USD'])
# 1.1）直接创建dictionary，比1）要更方便，用{}
rates_dict = {'USD': 3.8, 'PLN': 1, 'EUR': 4.3}
print(rates_dict)
for key, value in rates_dict.items(): #遍历 Dictionary，每次同时取出一个 Key和对应的 Value。
    print(key, value)#表达方式1
# 表达方式2
for key in rates_dict.keys():
    print(key, rates_dict[key])

print(type(rates_dict.keys()))
print(set(rates_dict.keys()))
print(rates_dict.values())
print(type(rates_dict.values()))
print(list(rates_dict.values()))

# 关于报错[]与get
my_exch_rate = rates_dict['GBP'] #会报错
my_exch_rate = rates_dict.get('GBP') #.get与[]不同，在key不存在时不会报错
my_exch_rate = rates_dict.get('GBP',2.5) #Default Value（默认值），仅当 Key 不存在时使用
print(my_exch_rate)
# endregion