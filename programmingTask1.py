print("Welcome to the Codetown Public Transport Data Collection System")


# Function checks if user has entered a non-negative integer
# User will be given the chance to re-enter the number if they make a mistake
# Returns the user input as an integer
def is_valid_input(user_input):
    while True:
        try:
            number = int(input(user_input))
        except ValueError:
            print("Please enter a non-negative integer.")
            continue

        if number < 0:
            print("Please enter a non-negative integer.")
            continue
        else:
            break
    return number


# Route number returned from function
route = is_valid_input("Please enter your bus route number: ")

# Checks if number of stops entered is non-negative integer
# User will be given the chance to re-enter the number if they make a mistake
# Then checks if the stops entered is greater than 2 (beginning and end of route)
while True:
    try:
        stops = int(input("How many stops on this route? "))
    except ValueError:
        print("Please enter a non-negative integer")
        continue

    if stops < 2:
        print("You must have at least 2 stops on your route")
        continue
    else:
        break

# Store values from each bus stop
passengers_on_bus = [0, ]
unhappy_customers = []
happy_customers = []

# Start looping from stop number 1 in the following while loop
stop_number = int(1)
# Start looping through passengers on the bus from the data of the previous stop
i = 0

# Loop through each stop to see how many passengers are waiting at each stop
# and how many passengers are getting off at each stop
while stops > 0:

    # Checks the values entered by the user to to make sure they are valid
    # Checks if it is an integer
    # Checks if it is non-negative
    # Checks to make sure nobody is getting on the bus at the end of the line
    while True:
        try:
            passengers_waiting = int(
                input("How many passengers were waiting at bus stop number " + str(stop_number) + "? "))
        except ValueError:
            print("Please enter a non-negative integer")
            continue

        if passengers_waiting < 0:
            print("Please enter a non-negative integer")
            continue

        if stops == 1 and passengers_waiting > 0:
            print("This is the end of the line, no passengers are waiting.")
            continue
        else:
            break

    # Checks the values entered by the user to to make sure they are valid
    # Checks if it is an integer
    # Checks if it is non-negative
    # Checks to make sure more people are not getting off the bus than were already on the bus
    while True:
        try:
            passengers_disembarking = int(
                input("How many passengers got off the bus at stop number " + str(stop_number) + "? "))
        except ValueError:
            print("Please enter a non-negative integer.")
            continue

        if passengers_disembarking < 0:
            print("Please enter a non-negative integer.")
            continue

        if passengers_on_bus[i] < passengers_disembarking:
            print("There were only " + str(passengers_on_bus[i]) + " passengers on the bus.")
            continue

        if stops == 1 and passengers_disembarking < passengers_on_bus[i]:
            print("This is the end of the line. All " + str(passengers_on_bus[i]) + " passengers must get off the bus.")
        else:
            break

    # Checks how many passengers are waiting at stop number 1
    # Calculates how many passengers get on the bus
    # Calculates how many passengers are left behind
    # Adds the values to the empty lists above
    if stop_number == 1:
        if passengers_waiting > 47:
            passengers_on_bus.append(47)
            left_behind = passengers_waiting - 47
            unhappy_customers.append(left_behind)
            happy_customers.append(47)
        else:
            on_bus = passengers_waiting
            passengers_on_bus.append(on_bus)
    else:

        # Checks how many people are on the bus
        # Calculates how many much room there is on the bus for waiting passengers
        # Adds the values to the empty lists above
        on_bus = passengers_on_bus[i] - passengers_disembarking + passengers_waiting
        if on_bus >= 47:
            passengers_on_bus.append(47)
            left_behind = on_bus - 47
            unhappy_customers.append(left_behind)
            made_it_on = passengers_waiting - left_behind
            happy_customers.append(made_it_on)
        else:
            passengers_on_bus.append(on_bus)
            happy_customers.append(passengers_waiting)
    # Adds one to the stop number to keep it going up by one each loop
    # Subtracts one from the stops as the bus moves through each stop and each loop
    # Adds one to i which checks how many passengers are on the bus during each loop
    stop_number += 1
    stops -= 1
    i += 1

else:

    # Calculates the ratio of happy to unhappy customers to 2 decimal places
    happy_to_unhappy_ratio = (sum(happy_customers) / (sum(unhappy_customers))).__round__(2)

    print("Route Number: " + str(route))
    print("Unhappy Customers: " + str(sum(unhappy_customers)))
    print("Happy Customers: " + str(sum(happy_customers)))
    print("Ratio of happy to unhappy customers: " + str(happy_to_unhappy_ratio))
