result = list(filter(lambda x: (x//100)**3+(x//10%10)**3+(x%10)**3 == x,range(100,1000)))#指数运算**的优先级高于向下取整除//  向下取整和取余同级
print(result)
