# region 3. list_sets_tuple_dicts
#创建列表（List），依次输出所有元素，包括重复数字。⭐️
arr_a = [3, 5, 7, 9, 5, 9]
for i in arr_a:
    print(i, end=' ')
print('\n' + '-' * 80)

#set()将list(列表)转换成set（集合），set不允许元素重复⭐️。是无序集合，不保证顺序
print('sets')
set_a = set(arr_a)
for i in set_a:
    print(i, end=' ')
print('\n' + '-' * 80)

#set 不支持索引，要转回list
arr_a = [3, 5, 7, 9, 5, 9]
print(arr_a[2])
print('\n' + '-' * 80)

# print(set_a[2]) - can't be done - Set 不支持索引（Indexing）⭐️，不能通过 [2] 访问元素。
#set + for loop
set_a = set(arr_a)
for i in set_a:
    print(i, end=' ')
print('\n' + '-' * 80)

# set 转为 list
list_a = list(set_a)
print(list_a)
print(list_a[2])
print('\n' + '-' * 80)

# 在set中添加或减少元素（缺代码）
list_a.append(8) #append()： 在列表（List）的末尾添加一个新元素8。
print(list_a)
list_a.insert(2, 100) #在第3位置处，插入数字‘100’
print(list_a)
print(type(list_a))
print('\n' + '-' * 80)

#remove & pop 移除数字
arr_a = [3, 5, 7, 9, 5, 9]
list_a = list(arr_a)
print(list_a)
list_a.remove(5) # 直接移除数字,按顺序移除第一个‘5’
print(list_a)

list_a.pop(1) #根据位置移除数字
print(list_a)

# region 4. list[]列表 VS tuple()元组。
# 共同点：都有序，都允许重复；都支持索引
# 不同点：tuple 不可以修改元素；添加元素；和append（）
t_1 = (2,56,86)
print(t_1)
print(type(t_1))
# endregion

