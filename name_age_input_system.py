name_age = {}

# Loop 1 is used to ask user for input
while True:
    
    while True:
        try:
            name = input("Please input your full name: ")
            age = input("Please input your age: ")
            break

        except:
            print("Error")