import random

money = 10

def round2(last):
    n1 = random.randint(1,6)
    n2 = random.randint(1,6)
    sum = n1+n2
    if sum == 7:
        print('庄赢')
        return -1
    elif(sum == last):
        print('玩家赢')
        return 1
    else:
        return round2(last)

while money>0:
    n1 = random.randint(1,6)
    n2 = random.randint(1,6)
    sum = n1+n2
    if sum == 7 or sum == 11:
        money += 1
        print('玩家赢')
    elif sum == 2 or sum == 3 or sum ==12:
        money += -1
        print('庄赢')
    else:
        money += round2(sum)

