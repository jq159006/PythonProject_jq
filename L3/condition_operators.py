#region 1. condition operators
from os import remove

s = 'absef'
match s: #检查 s 的值是什么。类似于 if，用于多种情况的判断。
        # match（case）更适合匹配某个值。if(else)更适合比较条件比如比大小
    case 'abcd':
        print('s is abcd') #如果 s == 'abcd'，就输出 s is abcd。
    case 'ab':
        print('s is ab')
    case _:
        print('s is not ab or abcd')
# endregion


