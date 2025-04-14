
# method to print divisors



def divisers(num):
    for i in range(1 , num+1):
        if (num % i == 0):
            print(i, end=" ")


divisers(100)