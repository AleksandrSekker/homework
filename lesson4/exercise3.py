number = int(input("Input number : "))
fibonacciSeries = [0,1]
if number>2:
	for i in range(2, number):
		nextElement = fibonacciSeries[i-1] + fibonacciSeries[i-2]
		fibonacciSeries.append(nextElement)
print(fibonacciSeries)