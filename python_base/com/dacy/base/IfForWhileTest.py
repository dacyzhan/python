# -*- coding:utf-8 -*-
'''
对python 基础 逻辑的学习 ，包含 if ，for  while

'''
# 测试 if elif else 用法
def testif():
    print('testif')
    a= 100
    if a < 5 :
        print('a<5:'+str(a))
    elif a> 5 and a<= 10 :
        print('a 5~10:' + str(a))
    else : print('不在范围内')

# 测试 for  循环
def testfor():
    print('testfor')

    # for 循环类似 java 中的 foreach
    names=['a','b','c']
    for name in names:
        print(name)

    numbs=[1,2,3,4,5]
    sum = 0
    for i in numbs:
        sum +=i
    print('sum:'+str(sum))
    # 生成 一个循环数组 [10, 12, 14, 16, 18, 20]
    print(range(10,21,2))
    # 生成 一个循环数组 [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(range(10))
    t = 0
    for i in range(10):
        t+= i
    print(t)

# 测试 while 循环
def testwhile():

    n = 0
    t = 100
    while t>n:
        n+=1
    print('n:'+str(n))

def testraw_input():
    # 注意 默认 使用  raw_input() 输入的为字符串类型，如果 要做数字判断先转换类型
    birth=int(raw_input('birth:'))
    if birth <2000:
        print('00前')
    else: print('00 后')


if __name__ =='__main__':
    testif()
    testfor()
    testwhile()
    testraw_input()