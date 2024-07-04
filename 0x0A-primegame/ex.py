#!/usr/bin/python3


def SieveOfEratosthenes(n):
    prime = [True for i in range(n+1)]
    # print(prime)
    p = 2
    
    while (p * p <= n):
        if (prime[p] == True):
            # print(prime[p])
            for i in range(p*p, n+1, p):
                prime[i] = False
        p += 1
    
    for p in range(2, n+1):
        if prime[p]:
            print(p)


if __name__ == '__main__':
    n =4
    SieveOfEratosthenes(n)
    

def winner(n):
    
    if n < 3:
        return 'Ben'
    else:
        return 'Maria'
    
if __name__ == '__main__':
    print(f"Winner: {winner(2)}")
    
i = 1
arr = [1, 2, 3]
# print(len(arr))
for i in range(len(arr)):
    p = [True for _ in range(i + 1)]
    print(p)

# while i <= 3:
#     print(i)
#     i += 1