import calculator

chouse_operator = input('Choose operator: ')
first_number = int(input('Chouse number: '))
second_number = int(input('Chouse second number: '))
if chouse_operator == 'add':
    print(calculator.add(first_number, second_number))
elif chouse_operator == 'division':
    print(calculator.division(first_number, second_number))
elif chouse_operator == 'subtraction':
    print(calculator.subtraction(first_number, second_number))
elif chouse_operator == 'multiplication':
    print(calculator.multiplication(first_number, second_number))

