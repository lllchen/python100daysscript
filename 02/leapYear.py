year = int(input('please enter year:'))
result = year % 400 == 0 or ((year % 100 != 0)and year % 4 == 0)
print(result)