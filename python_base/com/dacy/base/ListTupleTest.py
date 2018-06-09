#   -*- coding:utf-8 -*-

'''
List
Tuple
Python内置的一种数据类型是列表：list。list是一种有序的集合，可以随时添加和删除其中的元素。
类似java 中的数组 下标从 0 开始  可以是负的 ，负的则按照倒数的来
list 中元素类型不受限制，可不一样。
 classmates = ['Michael', 'Bob', 'Tracy']

Tuple
另一种有序列表叫元组：tuple。tuple和list非常类似，请注意，初始化格式不同，List 是 [],而 Tuple 是 ().
但是tuple一旦初始化就不能修改。
 classmates = ('Michael', 'Bob', 'Tracy')
'''

def testList ():

    classmates=['a','b','c']
    classmates.sort()
    print(classmates)


    # list 元素拼接
    classmates.append('d')
    print(classmates)

    # list 元素按照下标插入
    classmates.insert(2,'e')
    print(classmates)

    # 根据下标获取元素 下标从 0 开始
    print(classmates[1])
    print(classmates[-1])

    # 删除 list尾部的元素
    classmates.pop()
    print(classmates)

    # 删除 list指定下标的元素
    classmates.pop(0)
    print(classmates)

    # 替换 list 中的元素，直接按照下标元素进行赋值即可
    classmates[0] = 8
    print(classmates)

    # list 长度
    print(len(classmates))
    print('************************end ************************')

def testTuple ():
# 注意语法结构和 list 的区别只是 [] 和 () 之分。
    persons = ('wang','li','zhao')
# 输出某一元素下标
    print(persons.index('li'))
# 要定义一个只有1个元素的tuple,不能直接用 persons=(1),因为 ()既可以定义一个 tuple,同时也代表数字运算符中的 括号。
# 所以 定义时必须加一个逗号,，来消除歧义：
    tts=(1,)
    print(tts)






if __name__ == '__main__':
    testList()
    testTuple()