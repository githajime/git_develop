str1 = "月火水木金土"

str2 = input("検索文字列を入力：")

index = str1.find(str2)
if index != -1:
    print(str2 + "　が見つかりました")
    print("Index:", index)
else:
    print(str2 + "　が見つかりませんでした")
