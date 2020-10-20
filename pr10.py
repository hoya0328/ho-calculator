rest = "y"
count = 0
result = 0
while rest.lower() == "y":
    print("식을 선택하세요 \n1-더하기 \n2-빼기 \n3-곱하기 \n4-나누기")
    choice = input("계산식을 선택하세요(1/2/3/4) : ")
    if count == 0:
        num1 = int(input("첫 번째 수 :")
        num2 = int(input("두 번째 수 :"))

        if choice == "1":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")

        elif choice == "2":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")

        elif choice == "3":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")

        elif choice == "4":
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")

        else:
            print("잘못된 값입니다")
        rest = input("계속하시겠습니까? (y/n) :")

        count += 1

    else:
        num3 = int(input("추가 수를 입력하세요 :"))
        if choice == "1":
            print(f"{result} + {num3} = {result + num3}")
            result += num3

        elif choice == "2":
            print(f"{result} - {num3} = {result - num3}")
            result -= num2

        elif choice == "3":
            print(f"{result} * {num3} = {result * num3}")
            result *= num3

        elif choice == "4":
            print(f"{result} / {num3} = {result / num3}")
            result /= num2

        else:
            print("잘못된 값입니다")
        rest = input("계속하시겠습니까? (y/n) :")


