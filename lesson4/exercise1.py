input_number=int(input("Enter a number "))
result=1
for i in range(1, input_number +1):
    if i < input_number :
        result=result*(input_number +1)
print("Factorial of {} is {}".format(input_number, result))