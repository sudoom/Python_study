from decimal import *

getcontext().prec = 50


def fi(L0, L1, n):
    for i in range(n):
        L0, L1 = L1, L0 + L1
    return Decimal(L1), L0


print(fi(0, 1, 5))
import dec