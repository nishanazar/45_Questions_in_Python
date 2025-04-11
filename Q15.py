try:
    user_input = int(input("Enter a number: "))
    
    count = 1
    while count <= 10:
        print(f"{count} * 2 = {count * user_input}")
        count += 1

except ValueError:
    print("Please enter a valid number!")

