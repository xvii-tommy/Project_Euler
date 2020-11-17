# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
# answer: 6857

import math

class LPF:
    def __init__(self, value):
        self.lst = []
        self.templst = []
        self.value = value

    def factors(self):
        for i in range(2, self.value):
            if i**2 < self.value and self.value % i == 0:
                self.lst.append(i)
            elif i**2 > self.value:
                break
        for j in self.lst:
            x = self.value / j
            self.templst.append(x)
        for k in self.templst:
            self.lst.append(int(k))
        self.lst.sort()
        self.templst.clear()
        return(self.lst)

    def isprime(self, val):
        for p in range(2, val):
            if p**2 < val and val % p == 0:
                self.templst.append(val)
            elif p**2 > val:
                break
        return(self.templst)

    def largestprimefactor(self):
        f = self.factors()
        for i in f:
            x = 0
            self.isprime(i)
        for j in self.templst:
            for k in f:
                if j == k:
                    f.remove(k)
        print(f)
        print("the largest prime is ", f[-1])


lpf = LPF(600851475143)
lpf.largestprimefactor()