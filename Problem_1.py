# Listing all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

class multi:
    def __init__(self, value):
        self.lst = []
        self.value = value

    def multi3_5(self, target):
        for i in range(0, target):
            if i % 3 == 0 or i % 5 == 0:
                self.lst.append(i)
                print(i)
        print(self.lst)
        return self.lst

    def sumup(self):
        total = self.multi3_5(self.value)
        x = 0
        for i in total:
            x = x + i
        print(x)


T = multi(1000)
T.sumup()