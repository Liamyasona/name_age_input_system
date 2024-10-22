name_age = {}

# Loop 1 is used to ask user for input
while True:
    # Loop 2 is retry when user did not input a number
    while True:
        try:
            name = input("Please input your full name: ")
            age = int(input("Please input your age: "))
            break

        except:
            print("Error")

    if error == "n":
        break
    elif retry == "y":
        print("invalid")