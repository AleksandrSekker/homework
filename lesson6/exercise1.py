def func(t):
    """create three array (divisible by two, by thre and not divisible by this number), append data to this array and print in terminal"""
    
    divisible_by_two = []
    divisible_by_three = []
    not_divisible_by_three = []
    for i in t:
        if (i % 2 == 0):
            divisible_by_two.append(i)
        elif (i % 3 == 0):
            divisible_by_three.append(i)
        elif (i % 2 != 0 and i % 3 !=0):
            not_divisible_by_three.append(i)
    print('even numbers that are divisible by 2: ', divisible_by_two)
    print('odd numbers that are divisible by 3: ', divisible_by_three)
    print('numbers that are not divisible by 2 and 3: ', not_divisible_by_three)
func((1,2,3,4,5,6,7,8,9,10))