def countFactor(number):
    l=[1]
    i=1
    while True:
        if i == l[-1]:
            break
        else:
            i += 1
            if number%i == 0:
                l.extend([i,number%i])
    return l

result = [filter(lambda x ,,list(range(1,10001)))]