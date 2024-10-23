
user_name_age = []

# Loop 1 is used to ask user for input
while True:
    # Loop 2 is used for retry when user did not input letters
    while True:
        name = input("Please input your name: ")
        while not name.isalpha():
            print("ERROR! Please input your name again")
            name = input("Please input your name: ")
        

        # Check if the age is an integer
        while True:
            try:
                age = int(input("Please input your age: "))
                break 

            except ValueError:
                print("ERROR! Please input your age again.")
        