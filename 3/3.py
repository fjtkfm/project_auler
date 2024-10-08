# 試し割り方による回答
# https://note.nkmk.me/python-prime-factorization/
import sys


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a

args = sys.argv
print(prime_factorize(int(args[1])))
