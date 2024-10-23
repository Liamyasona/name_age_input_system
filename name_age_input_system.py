def is_valid_name(name):
    # Check if the name contains only letters and is not empty
    return name.isalpha() and len(name) > 0

user_name_age = []

# Loop 1 is used to ask user for input
while True:
    # Loop 2 is used for retry when user did not input a number
    while True:
        try:
            name = input("Please input your full name: ")
            break
            
        except:
            print("Error")
            
    while true:
        try:
            age = int(input("Please input your age: "))
            break 

        except ValueError:
            print("Error! Please input a number.")
