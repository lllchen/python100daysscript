def countFactor(number):
    l=[1,number]
    i=2
    while True:       
        if i >= l[-1]:
            break
        else:
            if number%i == 0:
                temp = list(set([i,int(number/i)]))
                temp.sort()
                l.extend(temp)
            i += 1       
    l.pop(1)
    print('number',number,':',l)
    return l

result = list(filter(lambda x :x == sum(countFactor(x)),list(range(2,10001))))
print(result)

