import random
firstnum = None
rannum = random.randint(1, 100)
count = 0
while firstnum != rannum:
    firstnum = int(input("Guess the number"))
    count += 1
    if(firstnum>rannum):
        print("bigger than rand")
    elif(firstnum<rannum):
        print("smaller than random")
print("You are right at "+str(count) +" times: "+ str(rannum))    
