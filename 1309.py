from random import randint
 
K = 10
a = []
for i in range(K):
    a.append(randint(1, 128))
print(a)
 
 
for i in range(K-1):
    for n in range(K-i-1):
        if a[n] > a[n+1]:
            a[n], a[n+1] = a[n+1], a[n]
 
print(a)