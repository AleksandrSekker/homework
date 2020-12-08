
for i in range(1, 100):
    if i % 2 != 1:
        continue
    print ("Odd: ", i)

[(print("Odd: ", i)) for i in range(1, 100) if i % 2 != 0]
