# -*- coding:utf-8 -*-
'''
dict 语法结构学习 类似 java 中的 map  d={'a':1,'b':2,'c':3,'d':4}
dict内部存放的顺序和key放入的顺序是没有关系的
set 语法结构学习    s =set([1,2,4,5,7])
'''
def testDict():
    print('********************testDict***************************')
    # 初始化 字典 dict 注意 是{}
    d={'a':1,'b':2,'c':3,'d':4}
    # 注意获取 字典的值的时候 key 是必须存在的，不存在会报错。如果对 key 赋值，多次赋值会替换前面赋值。
    print(d['a'])


    # 判断 字段 d 中是否存在某元素
    # 1. 用 in 如存在则返回 True ，不存在则返回 False
    print('a' in d)
    print('e' in d)
    # 2.用get('key') 如存在则返回 1 ，不存在则返回 None
    # 注意：返回None的时候Python的交互环境不显示结果。
    print(d.get('a'))
    print(d.get('e'))

    # 删除 字段中某一key 以及对应元素  pop()
    d.pop('a')
    print(d)
    # 插入 字典 d
    d['g']=6
    print(d)

# set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。
# set可以看成数学意义上的无序和无重复元素的集合，因此，两个set可以做数学意义上的交集、并集等操作：
def testset():
    print('***************************testset**************')
    # 初始化一个 set
    s =set([1,2,4,5,7])
    s1 =set([1,33,4,5,7])
    print('***')
    print(s & s1)
    print(s | s1)
    s.add(8)
    print(s)

    # 移除某一元素
    s.remove(1)
    print(s)



if __name__ == '__main__':
    testDict()
    testset()