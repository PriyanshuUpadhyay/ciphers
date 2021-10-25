import math

def euclid(num1, num2):
    if num2 == 0:
        return num1
    else:
        return euclid(num2, num1%num2)

def extendedEuclid(num1, num2):
    r1 = num1
    r2 = num2
    s1 = 1
    s2 = 0
    t1 = 0
    t2 = 1

    while(r2>0):
        q = math.floor(r1/r2)
        r = r1 - q * r2
        r1 = r2
        r2 = r
        s = s1 - q*s2
        s1  = s2
        s2 = s
        t = t1 - q * t2
        t1  = t2
        t2 = t
    
    return r1

n1, n2 = tuple(map(int, input("Enter two numbers to find gcd of: ").split()))
n1, n2 = abs(n1), abs(n2)
if n2>n1:
    temp = n1
    n1 = n2
    n2 = temp

print("GCD (",n1,",",n2,") using euclid's algorithm: ", euclid(n1, n2))
print("GCD (",n1,",",n2,") using extended euclid's algorithm: ", extendedEuclid(n1, n2))