# def is_even(n): 
#     return n%2 == 0





# def difference_in_ages(ages):
#     # your code here
#     youngest_age = min(ages)
#     oldest_age = max(ages)
#     difference = oldest_age - youngest_age
#     return (youngest_age, oldest_age, difference)






# def find_average(array):
#     return sum(array) / (len(array) or 1)






# def make_upper_case(strng):
#     return strng.upper()





# def length_of_sequence(arr, n):
#     try:
#         i = arr.index(n)
#         j = arr.index(n, i+1)
#         try:
#             arr.index(n, j+1)
#             return 0
#         except ValueError:
#             return j - i + 1
#     except ValueError:
#         return 0
    





# def tail_swap(ss):
#   a = [s.split(':') for s in ss]
#   a[0][1], a[1][1] = a[1][1], a[0][1]
#   return [':'.join(p) for p in a]