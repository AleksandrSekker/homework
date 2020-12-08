start_num = 0
while start_num <= 100:
    if start_num % 2 == 0:
        print('Even', start_num)
    start_num += 1

[(print('Even', even_number))for even_number in range(1, 101) if (even_number%2 == 0) ]