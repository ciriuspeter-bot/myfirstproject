with open("example.txt", "w", encoding="utf-8") as file:
    file.write("안녕하세요!\n")
    file.write("이것은 python으로 작성한 file입니다.")

# 파일 읽기
with open("example.txt", "r", encoding="utf-8") as file:
    content = file.read()
    print(content)