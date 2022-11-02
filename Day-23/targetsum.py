a = [1, 2, 3, 4, 5]
target = 5

found = 0
sum = 0
k = 0
length = len(a)
for i in range(k, length):

    sum += a[i + k]
    if sum == target:
        print(f"{k} index se {i} index tk")
        found = 1
    if sum > target:
        sum = 0
        k += 1
        i = 0
    if (i+k)>=length:
        sum = 0
        k += 1
        i = 0
        continue


if found == 0:
    print("Not Found")
