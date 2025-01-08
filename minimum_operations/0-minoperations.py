#!/usr/bin/python3
def minOperations(n):
    i = 2
    count = 2
    isOk = False
    while i <= n:
        print(i%n)
        print(count)
        if i%n == 0:
            if isOk!=True:
                isOk=True
                count+=1
            count += 1
            i+=2
            # return count + (n - i)/i
        else:
            i+=1
            count += 2
        print(count)
    return count

print(minOperations(12))