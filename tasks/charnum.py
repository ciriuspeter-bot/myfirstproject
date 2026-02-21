text = input("Enter the text")
cog = "aeiuAEIU"
count =  0
for ele in text:
    if ele in cog:
        count += 1
print("모음의 개수" + str(count))