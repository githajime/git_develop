end = int(input("Input last number:"))
sum = 0
counter = 0
while counter <= end:
    sum = sum + counter
    counter += 1

print("Sums up to " + str(end) + " is", sum)
