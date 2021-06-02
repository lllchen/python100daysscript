#代码复制自廖雪峰python教程的filter部分内容，初看没懂filter中参数的传递。
#思考良久终于明白了python中filter函数、lambda表达式、内部函数、闭包的参数传递过程。

def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    #return lambda x: x % n > 0 #廖雪峰的神仙写法，filter函数会把后面iterator中的每个元素直接给lambda中的形参，这是因为lambda相当于_not_divisible内定义的一个内部函数，在filter内第一个参数赋值为_not_divisible(n)时，
                                #由于_not_divisible有内部函数，且调用时函数名“_not_divisible”后只有一套括号，就相当于赋值为内部函数名了。因此会有这种效果，详见最后一行的测试代码。lambda和直接定义内部函数并返回闭包的方式结果相同。
                                #上面这两句话说的比较啰嗦，其实就是因为lambda相当于内部函数，return lambda相当于返回了内部函数的闭包，所以在filter中使用_not_divisible(n)时相当于把内部函数名放在了那里。
    def test(x):
        return x % n > 0
    return test#这里必须是return，内部函数的返回结果必须借助于上层函数的return才能返回，有点类似于递归中，下层的调用必须借助于上层的return层层返回才能到达初始调用点。


def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列

#for n in primes():
#    if n < 1000:
#        print(n)
#    else:
#        break

print(_not_divisible(2)(1))#这行代码测试了python中返回函数的调用，只要使用外层函数的函数名再追加一套调用括号即可。
