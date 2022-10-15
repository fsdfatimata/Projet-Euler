import math

def summation_primes(): 
  list_primes = []
  for n in range(2,2000001):
    if n%2 !=0:
      for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
          #print(n, 'equals', i, '*', n/i)
          break
      else:
        list_primes.append(n)
  #print(list_primes)
  print(sum(list_primes))
summation_primes()