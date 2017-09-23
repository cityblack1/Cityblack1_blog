from math import sqrt
import bisect

c = [2, ]


def su(n):
    global c
    m = 2
    q = 1
    if n == 1:
        return m
    while True:
        m += 1
        if check_zs(m):
            q += 1
        if q == n:
            return m


def check_zs(n):
    global c
    s = int(sqrt(n))
    p = bisect.bisect(c, s)
    for j in range(p):
        if n % c[j] == 0:
            # n 不是质数
            return False
    # n 是质数
    c.append(n)
    return True


print(su(522048))