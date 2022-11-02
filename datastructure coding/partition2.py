a = [4,1,6,2,5,9,7]
pivot = a[0]
left = 0
right = len(a)
fp = 0
for i in range(left+1,right):
    if a[i] >=pivot:
        continue
    fp+=1
    a[i],a[fp]=a[fp],a[i]
a[0],a[fp]=a[fp],a[0]

print(a)