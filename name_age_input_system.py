
names = []
ages = []

# Loop 1 is used to ask user for input
while True:
    # Loop 2 is used for retry when user did not input letters
    while True:
        name = input("Please input your name: ")
        while not name.isalpha and len(name) > 0():
            print("ERROR! Please enter a valid name.")
            name = input("Please input your name: ")
        
        # Check if the age is an integer
        while True:
            try:
                age = int(input("Please input your age: "))
                break 

            except ValueError:
                print("ERROR! Please input your age again.")

        names.append(name)
        ages.append(int(age))

        retry = input("Add another person? (Type Yes/No only): ")


        