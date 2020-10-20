def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def division(x, y):
    return x / y

print("어떤 계산을 하시겠습니까?")
print("1 - 더하기")
print("2 - 빼기")
print("3 - 곱하기")
print("4 - 나누기")

choice = input("번호를 선택해주세요(1/2/3/4) : ")

num1 = int(input("첫번째 숫자 :"))
num2 = int(input("두번째 숫자 :"))

if choice == "1":
    print(num1, "+", num2, "=", add(num1, num2))
    print("계산이 완료 되었습니다!")

elif choice == "2":
    print(num1, "-", num2, "=", subtract(num1, num2))
    print("계산이 완료 되었습니다!")

elif choice == "3":
    print(num1, "*", num2, "=", multiply(num1, num2))
    print("계산이 완료 되었습니다!")

elif choice == "4":
    print(num1, "/", num2, "=", division(num1, num2))
    print("계산이 완료 되었습니다!")

else:
    print("잘못된 형식을 입력하셨습니다.")
