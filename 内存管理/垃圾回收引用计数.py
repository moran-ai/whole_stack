import sys


class TestObject():
    def __init__(self):
        print(f'当前对象已被创建，当前对象的地址是{hex(id(self))}')


a = TestObject()
print(f'当前对象的引用计数为{sys.getrefcount(a)}')
b = a
print(f'当前对象的引用计数为{sys.getrefcount(a)}')
