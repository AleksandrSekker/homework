from functools import reduce
array = [1, 2, 3, 4, 5, 6, 7]

print(reduce(lambda a,b: a if (a > b) else b, array))