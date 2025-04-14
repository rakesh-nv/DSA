





def primnum():

    primes = []
    for i in range(2, 10):
        if i<2 :
            continue
        if i==2:
            primes.append(i)
            continue

        for x in range(2, i):
            if i % x == 0:
                break
        else:
            primes.append(i)

    return primes

print(primnum())