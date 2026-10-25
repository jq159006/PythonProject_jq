# region 2D lists-二维列表
points = [[1, 2], [4, 5], [7, 8]]
print(points)
el_5 = points[1][1] # 第2个框的第2位数字
print(el_5)
print(type(points))
print(type(points[2]))

for r in points:
    print(r)
    for c in r:
        print(c)
print('\n' + '-' * 80)
#-----------3x3--------------
points = [[1, 2, 5],
          [4, 5, 4],
          [7, 8, 8]]

print(points)
el_5 = points[1][1]
print(el_5)
print(type(points))
print(type(points[2]))

for r in points:
    print(r)
    for c in r:
        print(c)
print('\n' + '-' * 80)
# endregion

#region 2D lists-exercise
points = [[1, 2, 5],
          [4, 5, 4],
          [7, 8, 8]]
#sum_rows：先取一行r，再把这一行加起来c。
def sum_rows(my_list):
    result = [] #创建空列表，准备保存每行的结果。
    for r in my_list: #：每次从 my_list 中取出一个子列表，放进变量 r。
        total = 0 #很重要！准备开始计算当前这一行的总和，先从0开始。为了每一行能够做到单独求和
        for c in r: #从当前这一行 r 中，每次取出一个数字，放进变量 c。
            total = total + c
        result.append(total)
    return result
print(sum_rows(points))

#按列相加：先确定要计算哪一列，再从每一行中取出这一列的数字相加。
def sum_cols(my_list):
    result = []
    for i in range(len(my_list[0])): #i - （0,1,2）
        total = 0
        for r in my_list: #my list 还是行，但是r[i]提取出来的是正好是每一列的值。比如i=0,就是第一行提取第一个数+循环跳转到第二行提取第一个数依次类推
            total = total + r[i]
        result.append(total)
    return result
print(sum_cols(points))

#整个相加
def sum_list(my_list):
    total = 0
    for r in my_list: #外层循环：每次取出一整行。
        for c in r: #内层循环：从当前这一行中逐个取数字。
            total = total + c
    return total
print(sum_list(points))
# endregion