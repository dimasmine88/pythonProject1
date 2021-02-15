from math import sin, cos

# 1.1
def f1(x, y):
    return ((x ** 7) - 82 * y ** 2 + 84 + ((((y ** 8) / 39) + (x ** 7) - 67) / ((y ** 2) + 47 * x ** 5 + 15)) - (
                43 * x ** 3 - sin(y)))


print("{:.2e}".format(f1(-73, -15)))

#1.2
def f2(x):
    if x < 146: return (x**7)-82*(x**2)+84
    elif 146 <= x < 160: return ((x**3)/39)+(x**7)-67
    elif 160 <= x < 200: return (x**2)+47*(x**5)+15
    elif x >= 200: return 82((cos(x)+56*(x**6))**2)+58*(x**7)

print("{:.2e}".format(f2(78)))

#1.3
def p1(n):
    for i in range(1, n):
        return (45*(i**3)-85*(i**4))

def p2(n, m):
    for i in range(1,n):
        for j in range(1,m):
            return (sin(j)+((j**6)/15)-69)

def pf(n, m):
    return (p1(n)+74*p2(n,m))

print("{:.2e}".format(pf(83, 23)))
print("{:.2e}".format(pf(95, 37)))

#1.4
def f4(n):
    if n == 0: return 4
    elif n == 1: return 8
    return (cos(f4(n-2))+(1/58)*f4(n-1))

print("{:.2e}".format(f4(5)))