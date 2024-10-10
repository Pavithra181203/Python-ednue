def classify_age():
    age = int(input("Please enter your age: "))
    if age < 0:
        print("Invalid input! Age cannot be negative.")
    elif age < 18:
        print("Minor")

    elif age <= 65:
        print("Adult")

    elif age >=65:
        print("Senior Citizen")
    else:
        print("Invalid input! Please enter a numeric value.")

classify_age()

