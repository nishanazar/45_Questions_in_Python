try: 

    user_input = int(input("Enter a number: "))

    if user_input % 2 == 0:
        print("even number:", user_input)
    else:
        print("odd number:", user_input)
        
except ValueError:
    print("Please enter a valid number!")