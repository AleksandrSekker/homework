number = int(input("Input number : "))
fibonacciSeries = [0,1]
[fibonacciSeries.append(fibonacciSeries[k-1]+fibonacciSeries[k-2]) for k in range(2,number)]
if number<=0:
   print('Please positive numbers only')
elif number == 1:
   fibonacciSeries = [fibonacciSeries[0]]
   print(fibonacciSeries)
else:
   print(fibonacciSeries)