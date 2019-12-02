#Lattice Paths, Project Euler problem number 15
#Starting from the top left corner and only being able to move
#to the right and down to get to the bottom right corner, how
#many routes are there on a 20x20 grid

from math import factorial

def num(k,p):
    return factorial(k)/(factorial(p)*factorial(k-p))

print('The amount of Lattice Paths is '+str(num(20+20,20)))





    
