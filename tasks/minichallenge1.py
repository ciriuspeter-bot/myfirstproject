test2 = ["apple", "banana", "cherry", "date", "elderberry"]
words = []
n = len(test2)
for word in test2:
    words.append(len(word))
print(words)
for i in range(n-1):
    for j in range(n-1-i):
        if words[j]>words[j+1]:
            test2[j], test2[j+1] = test2[j+1], test2[j]
            words[j], words[j+1] = words[j+1], words[j]
        else:
            print("swap")
print(words)
print(test2)