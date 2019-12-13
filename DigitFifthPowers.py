#Project Euler Problem 30: Digit Fifth Powers
#There are only three numbers that can be written as the sum of fourth
#powers of their digits
#1634 = 1^4 + 6^4 + 3^4 + 4^4
#8208 = 9^4 + 4^4 + 7^4 + 4^4
#9474 = 9^4 + 4^4 + 7^4 + 4^4
#the sum of these is 19316.
#Find the sum of all the numbers that can be written as the sum of fifth
#powers of their digits.

solution = 0
for i in range(2,5*9**5+1):
    if sum([int(x)**5 for x in str(i)]) == i:
        solution += i
print(solution)
 
 



