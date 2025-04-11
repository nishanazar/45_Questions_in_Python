try:
    user_input: int = int(input("Enter a number: "))
    if user_input == 0:
        print(f"The number {user_input} is zero.")
    elif user_input > 0:
        print(f"The number {user_input} is a positive number.")
    else:
        print(f"The number {user_input} is a negative number.")

except ValueError:
    print("Enter a valid number")

