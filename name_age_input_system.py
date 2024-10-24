# List for the entered names and ages
names = []
ages = []

# Loop 1 to ask user for input
while True:
    print("Name-Age Input System")
    # Loop 2 for name input
    while True:
        name = input("Please input your name: ")
        if any(char.isdigit() for char in name):
            print("ERROR! Please input your name again.")
        else:
            break  # Exit this loop if the name is valid

    # Loop for age input
    while True:
        try:
            age = int(input("Please input your age: "))
            if age < 0:
                raise ValueError
            break  # Exit this loop if the age is valid
        except ValueError:
            print("ERROR! Please input your age again.")

    # Store the data
    names.append(name)
    ages.append(age)

    # After input, retry message if another person will be added on the list
    retry = input("Add another person on the list? (Type yes/no only): ").strip().lower()
    if retry == "no":
        break  # Break if the user inputs "no"

# Check for the oldest person
if ages:
    oldest_index = ages.index(max(ages))  # Find the index of the person with the oldest age
    oldest_name = names[oldest_index]
    oldest_age = ages[oldest_index]
    print("The oldest person on the list is: ")
    print(f"{oldest_name}")
    print(f"{oldest_age}")

