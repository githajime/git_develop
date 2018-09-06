
age = int(input("年齢を入力"))

if age >= 0:
    if age <3:
        print("無料")
    elif age < 13:
        print("200円")
    elif age < 65:
        print("400円")
    else:
        print("無料")
else:
    print("正の値を入力")
