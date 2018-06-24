# -*- coding:utf-8 -*-
# 上面的语句为设置中文编码，还可以 为 # coding = utf-8
'''
三个 单引号 表示块注释
本节为 数据类型和变量 练习
'''


# 测试函数
def test():
    print('hello , world ')
# Python允许用'''...'''的格式表示多行内容
    print('''
    lin1
    lin2
    lin3''')

    print("""
    a
    b
    c
    """)

def testString():
    # \' 表示 ' ,斜杠为转义符
    print('I\'am ok.')

# 转义字符\可以转义很多字符，比如\n表示换行，\t表示制表符，字符\本身也要转义，所以\\表示的字符就是\
    print('\\\t\\')
    print('\\\n\\')

# Python允许用r''表示''内部的字符串默认不转义
    print(r'\\')


# 布尔值可以用and、or和not运算。
    print( True and False)
    print( True and True)
    print( True or False)
    print( not True)
    print( not False)
    print( not 1>3)


# 无需定义变量类型 类型会根据赋值转变
# 显式类型转换的格式为type(value)，type为目标类型，value为要转换的值 比如下面的 str(a)
    a= 123
    print('a:'+str(a))
    a='ABC'
    print('a:'+a)
    a = 'ABC'
    b = a
    a = 'XYZ'
    print(b)

    print(10/3)
    print(10//3)

# main 函数
if __name__=='__main__':
    test()
    testString()