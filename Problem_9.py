import math
""" def Pythagorean(a, b):
     c = math.sqrt(a ** 2 + b ** 2)
     pyth =  a + b + c
     prod = a*b*c   
     print(prod) 
     print(pyth)
Pythagorean(3, 4) """

#create a function(n)
for a in range(1, 1000):
    for b in range(1, 1000):
        c = (1000 - a) - b
        #print(c)
        if a < b < c:
            if a**2 + b**2 == c**2:
                prod = a * b * c
                print(f'the Pythagorean triplet is given by: {a}, {b}, {c}')
                print(f'prod = {prod}')
      
       


