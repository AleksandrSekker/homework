def check_odd_even(number):
    # n = int(input("Input entire number: "))
    while type(number) != int:
        try:
            number = int(number)
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
# cheсk_odd_even(-6)
check_odd_even("gth")
# cheсk_odd_even(0)