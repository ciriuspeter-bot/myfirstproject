# 입력 예
data = [3, 1, 2, 3, 2, 4, 5, 1, 6, 4]

# 풀이
def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates(data))  # [3, 1, 2, 4, 5, 6]