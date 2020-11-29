#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

score = 0

for i in range(20, 999999999, 20):
    for j in range(2, 20):
        if i % j != 0:
            score = 0
            break
        else:
            score = score + 1
            if score >= 19:
                print(i)
