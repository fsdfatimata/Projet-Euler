# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

# Find the largest palindrome made from the product of two 3-digit numbers


def largest_palindrome():
    mes_palindromes = []
    factor = {}
    n = 999
    for i in range(n, 101, -1):
        for j in range(i, 101, -1):
                pal = i*j
                if str(pal) == str(pal)[::-1]:
                    #print(f'{pal} = {i} x {j}')
                    factor[f'{pal}'] = f'{i} x {j}'
                    mes_palindromes.append(pal)
    max_pal = max(mes_palindromes)
    print(max_pal)
    print(f'{max_pal} = {factor.get(f"{max_pal}")}')
    
largest_palindrome()

#                 ma_chaine = str(n)
#                 for k in ma_chaine:
#                     ma_list.append(k)
#         if list(reversed(ma_list)) == ma_list:
#             print(ma_list)
#         ma_list=[]
#         break
#     print(f'{n} = {j} x {k}')
    
# largest_palindrome()
