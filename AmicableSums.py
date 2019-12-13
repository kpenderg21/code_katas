#Project Euler Number 21: Ammicable Numbers
#Let d(n) be defined as the sum of proper divisors of n(numbers less than n
#which divide evenly into n).
#If d(a) = b and d(b) = a, where a is not equal to b, then a and b are an
#amicable pair and each of a and b are called amicable numbers.
#Evaluate the sum of all the amicable numbers under 1000.

import math

def sum_div(n):
    s = 0
    for i in range(1,n):
        if n % i == 0: s +=i
    return s

def amicable_pairs(low,high):
    L = [sum_div(i) for i in range(low,high + 1)]
    pairs = []
    for i in range(high - low + 1):
        ind = L[i]
        if i + low < ind and low <= ind and ind <= high and L[ind - low] == i + low:
            pairs.append([i+low,ind])
    return pairs

def sum_pairs(pairs):
    return sum([sum(pair) for pair in pairs])


ans = sum_pairs(amicable_pairs(1,10000))

print(ans)
    
