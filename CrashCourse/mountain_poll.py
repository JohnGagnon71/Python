responses = {}
polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb some day? ")

    responses[name] = response
    
    repeat = input("Would you like another person to respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    
    print("\n--- Poll Results ---")
    for name, response in responses.items():
        print(f"{name} would like to climb {response}.")

        