number = input("Please enter the layers of pyramid.\n")
number = int(number)
for el in range(1, number+1):
    print(" "*(number-el)+"* "*el)