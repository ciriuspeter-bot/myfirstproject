number = input("Enter the number")
firstnum = 1
for i in range(1, int(number)+1):
    firstnum *= i
print(firstnum)