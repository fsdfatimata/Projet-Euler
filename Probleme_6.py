# The sum of the squares of the first ten natural numbers is,
# 1**2
# The square of the sum of the first ten natural numbers is,
# 1
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
# 1
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.


def dif():
    list1 = []
    list2 = []
    for i in range (1, 101):
        list1.append(i)
        j = i**2
        list2.append(j) 
    squares_sum  = sum(list2) 
    #print(s1)
    #for j in range(1, 101):
    sum_squares = (sum(list1))**2
    print(f'{sum_squares } - {squares_sum} = {sum_squares - squares_sum}')
dif()
      

