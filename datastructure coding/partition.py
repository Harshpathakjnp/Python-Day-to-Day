a = [6, 1, 5,5, 9, 8, 2, 7, 3,5]
pivot = a[0]
j = 1
for i in range(1, len(a)):
    if a[i] < pivot:
        a[i], a[j] = a[j], a[i]
        j += 1
a[0], a[j - 1] = a[j - 1], a[0]
print(a)
