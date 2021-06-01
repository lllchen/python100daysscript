#这是一个生成器不能使用递归函数的例证，本想写个永不停止的斐波那契数列生成式，但是失败了，因为递归函数下一层yield的结果只能被上一层调用，不能直接给for...in...里的next()

def fibonacci(a=0,b=1):
    print('a:',a)
    yield b
    a , b = b , a+b
    #print('a')
    r = next(fibonacci(a,b))
    print('r:',r)
    yield r

f = fibonacci()
for i in range(10):
    print('i:',i)
    print('数列',next(f))

