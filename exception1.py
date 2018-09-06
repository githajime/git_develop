import sys

try:
    score = int(input("Input your score:"))
except:
    print("*Input number")
    sys.exit()
else:
    print("Your Score:", score)
    if score >= 80:
        print("Pass")
    else:
        print("Fail")
