def simple_gen():
    yield '가'
    yield '나'
    yield '다'

gen = simple_gen()

print(next(gen))  # 가
print(next(gen))  # 나
print(next(gen))  # 다
print(next(gen))  # StopIteration 예외