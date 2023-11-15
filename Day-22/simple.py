#fibbonacci series 0 1 1 2 3 5 8 13 21
n = 10
a = 0
b = 1
c = 0
for i in range(1,n+1):
    a = b
    b = c
    c = a + b
    print(c,end=" ")