import math

input_number=int(input("Enter a number "))

# first version
result=1
for i in range(1, int(input_number) +1):
        result=result*i
print("Factorial of {} is {}".format(input_number, result))

# second version
print(math.factorial(int(input_number)))
