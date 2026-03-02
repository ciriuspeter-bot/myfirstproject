scores = {"철수": 85, "영희": 92, "민수": 78, "지연": 95, "준호": 88}

# 풀이 (값 기준 내림차순 정렬)
sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
print(sorted_scores)
# {'지연': 95, '영희': 92, '준호': 88, '철수': 85, '민수': 78}