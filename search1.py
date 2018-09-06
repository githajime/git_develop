
str1 = "月火水木金土"

str2 = input("検索文字列を入力：")

if str2 in str1:
    print(str2 + "　が見つかりました")
else:
    print(str2 + "　が見つかりませんでした")
