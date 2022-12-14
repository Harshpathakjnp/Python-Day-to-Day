a = [2, 9, 7, 13, 19, 8]
for i in range(len(a)):
    minm = i
    for j in range(i + 1, len(a)):
        if a[minm] > a[j]:
            minm = j
    a[minm], a[i] = a[i], a[minm]
    print(a)