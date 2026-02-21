try:
    num1 = input("Enter the first number")
    num2 = input("Enter the second number")
    print(str(num1)+"/"+str(num2))
    result = int(num1)/int(num2)
    print("="+str(result))
except ZeroDivisionError:
    print("나누기를 진행할수 없습니다")
except ValueError:
    print("수자를 입력해주십시오")