#


x = [8, 6, 9, 3, 3, 6, 7]
n = 7
output=[0 for i in range(n)]
f = [0 for i in range(10)]
for i in x:
    f[i] += 1
for i in range(1, 10):
    f[i] = f[i] + f[i - 1]
print(f)
for i in range(n-1,-1,-1):
    value=x[i]
    pos=f[value]
    output[pos-1]=value
    f[value]-=1
print(output)
