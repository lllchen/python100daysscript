def fibona():
    a,b=0,1
    while True:
        yield b
        a,b=b,a+b

a = fibona()
for i in range(10):
    print(i,next(a))