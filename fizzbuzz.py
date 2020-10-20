number = int(input("Please write a number between 1 and 100: "))
if number > 100:
    number = int(input("Please provide a number smaller than 100: "))
print(number, "\n")

for i in range(1, number+1):
    if i % 3 == 0 and i % 5 == 0:
        print("fizzbuzz")
    elif i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    else:
        print(i)
