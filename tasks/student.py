student = {"a" : 8, "b" : 9, "c" : 10, "d" : 8}
for key, value in student.items():
    print(key + " : " + str(value) + "scores")
average = sum(student.values())/len(student)    
print(average)