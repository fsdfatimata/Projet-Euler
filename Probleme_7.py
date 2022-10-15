""" By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number? """

# set_st_prime = []
# var = []
# def st_prime(): 
#   for n in range(2, 14):
#       for i in range(2,n):
#         if (n % i) == 0:
#           #print(n, 'equals', i, '*', n/i)
#           break
#       else:
#         set_st_prime.append(n)
#   #print(set_st_prime)
#   for j in range(1, len(set_st_prime) + 1):
#     var.append(j)
#   #print(var)
#   dictionary = dict(zip(var, set_st_prime))
#   print(dictionary)
#   print(dictionary[6])
# st_prime()
import time
import math
start = time.perf_counter()
 
n_prime = 10001
n = 1
count  = 0
while (count < n_prime):
  n = n + 1
  for i in range(2,n+1):
    if (n % i== 0): 
      break
  if (i == n):
    count= count + 1
duree = time.perf_counter() - start
print(duree)
print(n)

