

try :
    user_input = int(input("enter a number: "))
    print(f"{user_input} is a number")

except ValueError:
    print("It's not a number")
