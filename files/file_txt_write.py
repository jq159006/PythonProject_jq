# region 8.writing a file⭐️
import os
my_file = os.path.join('../data', 'fileout.txt')

f = open(my_file, 'w')  # Open the file in write mode 以写入模式打开文件
f.write('Hello World\n')
f.write('Python here\n')
f.write('At SGH\n')
f.close()
# endregion

# region 8.2.Buffer & flush()（缓冲区）⭐️⭐️
# 文件真正写入存储系统前，数据临时停留的一个空间。执行 f.close() 后，内容才出现在文件中。
f = open(my_file, 'w')
f.write('First line\n')
f.write('Second line\n')
f.flush()  # Flush buffered data 刷新缓冲区中的数据
f.write('Third line\n')
f.close()
# endregion

# region 8.3.Append Mode（追加模式）
with open(my_file, 'a') as f:  # Open the file in append mode 以追加模式打开文件
    f.write('Another line\n')
# endregion