#   -*- coding:utf-8 -*-
import os
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
    # classmates[0:3]
    # 表示，从索引0开始取，直到索引3为止，但不包括索引3。即索引0，1，2，正好是3个元素。
    print(classmates[0:2])   # 切片 Slice 结果为 ['a', 'b']
    L=[0,1,2,3,4,5,6,7,8,9]



    L= list(range(50))
    print(L[:10])   # 下标 从0 到 10
    print(L[-10:])  # 下标 从倒数第十 到末尾
    print(L[10:20])  # 下标 从10 到 20
    print(L[::2])  # 每2个元素取一个
    print(L[10:20:2])  # 下标 从10 到 20(不包含20) ,每2个元素取一个


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

# 列表生成式
def TestList():
    #print(list(range(1,11))) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    L=[]
    for x in range(1,11):
        L.append(x*x)
    print(L) #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    T=[x*x for x in range(1,11)]
    print(T)  #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

    Y= [x * x for x in range(1, 11) if x%2==0]
    print(Y)  #  print(T)

    H = [ m+n for m in 'abc' for n in 'XYZ']
    print(H)  # ['aX', 'aY', 'aZ', 'bX', 'bY', 'bZ', 'cX', 'cY', 'cZ']
    #列出当前目录下的所有文件和目录名
    G = [d for d in os.listdir('.')]
    print(G)

    #
    d ={'a':'x','b':'y','c':'z'}
    for k, v in d.items():
        print(k + '='+ v  )




'''
练习
利用切片操作，实现一个trim()函数，去除字符串首尾的空格，注意不要调用str的strip()方法：
'''
def trim(x):
    if(len(x)==0):
        return x
    elif x[0]==' ':
        return trim(x[1:])
    elif x[-1]==' ':
        return trim(x[:-1])
    return x







if __name__ == '__main__':
    # testList()
    # testTuple()
    # print(trim('hello  '))
    # print(trim('  hello'))
    # print(trim('  hello  '))
    # print(trim(''))
    # print(trim('    '))
    TestList()