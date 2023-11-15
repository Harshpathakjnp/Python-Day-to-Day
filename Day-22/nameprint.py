import collections
f = False
val = []
arr = [1,2,3,4,5,4,3,2,1]
a = collections.Counter(arr)
for i in a.keys():
    if a[i] == 1:
        f = True
        val.append(a[i])
if f:
    print(val)
else:
    ("Not Found")