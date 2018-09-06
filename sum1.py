end = int(input("Input last number:"))

sum = 0
for num in range(1, end + 1):
    sum += num

print("Sums up to" + str(end) + "=", sum)
