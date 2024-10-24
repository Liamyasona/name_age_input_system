#List for the entered names and ages
names = []
ages = []

# Loop 1 is used to ask user for input
while True:
    # Loop 2 is used for retry when user did not input letters
    while True:
        name = input("Please input your name: ")
        while not len(name) > 0 and name.isalpha():
            print("ERROR! Please enter a valid name.")
            name = input("Please input your name: ")
        
        # Check if the age is an integer
        while True:
            try:
                age = int(input("Please input your age: "))
                break 

            except ValueError:
                print("ERROR! Please input your age again.")

            # Store in the masterlist all data
            names.append(name)
            ages.append(int(age))

        # Retry message
        retry = input("Add another person? (Type Yes/No only): ")
        if retry == "Yes":
            break
    
    if ages:
        oldest_index = ages.index(max(ages))  # Find the index of the oldest age
        oldest_name = names[oldest_index]
        oldest_age = ages[oldest_index]

    




        