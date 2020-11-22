#A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
# answer:

class PAL:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
        self.lst = []

    def palindrom(self):
        for x in range(self.val1, 1, -1):
            for y in range(self.val2, 1, -1):
                num = x * y
                value = str(num)
                if value[0] == value[-1]:
                    self.lst.append(value)
        self.ispal()


    def ispal(self):
        for i in self.lst:
            x = str(i)
            fhalf = x[:round(len(x) / 2)]
            shalf = reversed(x[round(len(x) / 2):])
            for j, k in fhalf, shalf:
                print(x, j,k)






p = PAL(99, 99)
p.palindrom()

