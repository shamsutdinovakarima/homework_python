import string
import random

s = string.ascii_letters
def let(s):
    print(random.choice(s))
    
let(s)

def create(num):
    result = ''
    for i in range (num):
        result+=random.choice(string.ascii_letters)
    return result


def count_str(s):
    big = 0
    small = 0
    for sym in s:
        if sym.isupper():
            big += 1
        else:
            small += 1
    if big > small:
        return 1
    elif small > big:
        return 0
    else: 
        return -1
a = create(8)
print(a)                
print(count_str(a))  

s = string.ascii_letters
def let(s):
    print(random.choice(s))
    
let(s)

def f(length, num):
    return [create(length) for i in range(num)]
    
print(f(8, 10))

def percents(f):
    uppers = lowers = 0
    for i in f:
        if i.isalpha():
            if i.islower():
                lowers += 1
            else:
                uppers += 1
    y = uppers + lowers
    x = (uppers*100)//y
    return {'upper':x,'lower':100-x};
print(percents(f(8, 10)))