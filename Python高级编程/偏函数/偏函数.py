import functools

int_2 = functools.partial(int, base=2)  # base 代表进制
print(int_2('10000'))
