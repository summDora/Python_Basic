# -*- coding: UTF-8 -*-
# coding=utf-8
# 中文编码 第一种处理方式：文件顶部添加 # -*- coding: UTF-8 -*-

#  严格缩进：
if True:
    print ('true')
else:
    print ('false')
#print ('false')
#  没有严格缩进，在执行时会报错
#   File "F:/summer_dora_workspace/Python_S_Space/basic.py", line 5
#     print ('false')
#     ^
# IndentationError: unexpected indent


# 多行语句：
total = 1+\
        2+\
        3
total=1+2+3+4
print (total)
# Python语句中一般以新行作为语句的结束符。
# 但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：

# 单行注释
"""
多行注释
"""
'''
多行注释
'''

'''
函数之间或类的方法之间用空行分隔，表示一段新的代码的开始
类和函数入口之间也用一行空行分隔，以突出函数入口的开始
'''

'''
程序执行后就会等待用户输入，按回车键后就会退出
'''

raw_input("按下 enter 键退出，其他任意键显示...\n")


