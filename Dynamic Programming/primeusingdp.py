primes = [2, 3, 5]
i = 5
t = 2
while i <= 50:
    print(i)
    i += t
    t = 6 - t
    root = int(i**0.5)
    count = 0
    for j in range(len(primes)):
        if i % primes[j] != 0:
            count += 1
        else:
            break

    if count == len(primes):
        primes.append(i)
print(primes)
