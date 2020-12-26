def day_array(num):
    weekDays = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
    try:
        num = int(num)
        if num > 7 or num <= 0:
            raise ValueError(0)     
        return weekDays[num-1]             
    except ValueError as e:
        print("Please enter correct number. ", e)

day = day_array(input("Please, enter the number: "))
print(day)