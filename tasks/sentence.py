strs = "I have a apple and abocarodo."
new_str = strs.split()
length = max(new_str, key=len)
print(length+" "+str(len(length)))