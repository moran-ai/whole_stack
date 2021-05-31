# Iterable:可迭代对象 能够通过for循环来遍历里面的元素的对象
# 可以被next()函数调用并不断返回下一个值的对象称为迭代器
# 使用isinstance()方法判断一个对象是否是迭代器
from collections.abc import Iterable
from collections.abc import Iterator

a = {}
b = (1,)
c = []

def tesdt1(args):
    if isinstance(args, Iterable):
        print('是可迭代对象')
    else:
        print('不是可迭代对象')

# tesdt1(1)
def tesdt2(args):
    if isinstance(args, Iterator):
        print('是可迭代对象')
    else:
        print('不是可迭代对象')
# tesdt2((x for x in range(32)))

# 使用iter()将list,dict,str变为迭代器
tesdt2(iter(a))