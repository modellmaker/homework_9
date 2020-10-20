miles = 0.6213688756
another = "yes"
print("Hello, I'm a unit converter program. I convert kilometers into miles.")

while True:
    if another == "yes":
        km = int(input("Please enter the number of kilometers: "))
        print(km, "km is", float(km)*miles, "miles.")
        another = input("Would You like to continue? (Yes/No): ")
        another = another.lower()
    else:
        print("Goodbye!")
        break
