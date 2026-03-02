def numChar(strr):
    if not strr:
        return ""     
    n = len(strr)
    count = 1
    result = ""
    for i in range(n-1):
        if strr[i] == strr[i+1]:
            count += 1
        else:
            result += strr[i]+str(count)
            count = 1
    result +=  strr[-1] + str(count)
    return result
print(numChar("aaabccccccc"))
