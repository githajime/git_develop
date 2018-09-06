secret = "foo"

while True:
    word = input("Input your secret word:")
    if word == secret:
        print("Correct")
        break
    else:
        print("Inccorect")
        
