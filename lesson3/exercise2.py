four_digit_number = int(input('Enter a four digit number : '))
array_four_digit_number = [int(x) for x in str(four_digit_number)]

sum_four_number = sum(array_four_digit_number)

reversed = int(str(four_digit_number)[::-1])
sorting = sorted(array_four_digit_number)

print("Reversed: ", reversed)
print("Sum of numbers: ", sum_four_number)
print("Sorting: ", sorting[0], sorting[1], sorting[2], sorting[3])