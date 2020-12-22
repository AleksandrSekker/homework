def check_odd_even(number):
    # n = int(input("Input entire number: "))
    while type(number) != int or number < 0:
        try:
            number = int(number)
            if number <= 0:
                raise ValueError('Cant be less than 0')
            break
        except ValueError as e:
            print(e)
            number = input("Input entire number:\n ")
        except KeyboardInterrupt as e:
            print(e)
        
    if number % 2 == 0:
        print("Entered number is even")
    else:
        print("Entered number is odd")

check_odd_even(15)
check_odd_even(-6)
# check_odd_even("gth")
# cheсk_odd_even(0)