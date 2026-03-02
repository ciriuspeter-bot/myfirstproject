list1 = [1, 3, 5, 7, 9]
list2 = [2, 4, 6, 8, 10]

results = []
for x, y in zip(list1, list2):
    results.append(x)
    results.append(y)
print(results)