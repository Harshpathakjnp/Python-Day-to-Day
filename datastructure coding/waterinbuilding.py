a = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
n = 12
rm = max(a)
lm = a[0]
x = 0
sum = 0
t = ("Left Max", "Value", "Right Max", "Water")
print(t)
for i in range(1, n):
    if lm < a[i - 1]:
        lm = a[i - 1]
    if a[i - 1] == rm:
        rm = a[n - 1]
        for j in range(i + 1, n):
            if rm < a[j]:
                rm = a[j]

    water = min(lm, rm)
    water = water - a[i]
    water = max(water, 0)
    sum += water
    t = (lm, a[i], rm, water)
    print(t)
print("Answer ", sum)
