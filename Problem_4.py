#A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.
# answer:

class PALINDROM:
    def __init__(self, val1, val2):
        self.val1 = val1
        self.val2 = val2
        self.lst = []
        self.pal_lst = []
        self.answer = []

    def find_values(self):
        for x in range(self.val1, 100, -1):
            for y in range(self.val2, 100, -1):
                num = x * y
                value = str(num)
                if value[0] == value[-1] and value[1] == value[-2]:
                    if value not in self.lst:
                        self.lst.append(value)
        return self.lst

    def reversepal(self, pal):
        for i in pal:
            i = i[::-1]
            self.pal_lst.append(i)
        return self.pal_lst

    def find_palindroms(self):
        x = self.find_values()
        y = self.reversepal(x)
        for i in range(len(x)):
            if x[i] == y[i]:
                self.answer.append(x[i])
        for j in self.answer:
            a = [int(i) for i in self.answer]
        a.sort()
        print(a)
        print("The biggest palindrom is", a[-1])


p = PALINDROM(999, 999)
p.find_palindroms()

