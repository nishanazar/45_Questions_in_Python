try:

    user_input : int = int(input("Enter a number: "))
    print(f"Multiples of 30 from 1 to {user_input}:")
    
    for i in range(1, 30+1):
        if i % user_input == 0:
            print(i)

except ValueError:
    print("Please enter valid number")