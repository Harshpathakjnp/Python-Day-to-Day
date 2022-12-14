# insertion sort takes advantage of any ordering already present in the array it adjusted only the out-of order elements
# insertion sort is the method that card players used
# insertion is widely used in industrial grade application
a = [2, 4, 5, 6, 3]
n = len(a)
for i in range(n - 1):
    if a[i] <= a[i + 1]:
        continue
    temp = a[i + 1]
    j = i + 1
    while j >= 1 and a[j - 1] > temp:
        a[j] = a[j - 1]
        j -= 1
    a[j] = temp
print(a)
