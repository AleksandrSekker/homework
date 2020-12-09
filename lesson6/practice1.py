
count = int(input('Please enter a count element '))
number_list = [int(input('Please enter a number ')) for i in range(count)] 
print("Minimum number: {}".format(min(number_list)))
print("Maximum number: {}".format(max(number_list)))

