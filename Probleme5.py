# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# def smallest_number(n):
#   i = 1
#   while i< 10:
#     while n % i == 0:
#      print(i)
#      i = i + 1
#print(f'{n} % {k} = {n % k}')
        #multiples.append(k)
      #print(multiples)
        #dict[f'{n}'] = f'{multiples}'
        
        #print(dict)
      #print(f' result is  {dict.get(valeurs)}')


# smallest_number(2520)
from math import factorial

from operator import mul



def smallest_number():
  multiples = []
  restes = set()
  #max_rest = 20
  ppcm = factorial(10)
  n_initial = 2520
  #for n in range (n_initial, factorial(max_rest) + 1):
  for n in range (2510, 2530):
      for k in range (2, 11):
          if n % k == 0 :
            restes.add(k)
            #print()
            if restes == set(range(2, 11)):
               multiples.append(n)
               break
          else:
            restes = set()
            break        
      if multiples:
          ppcm = min(multiples)
          break
  print(ppcm)
  print(restes)
smallest_number()
      

