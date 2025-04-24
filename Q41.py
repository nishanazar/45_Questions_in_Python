import random 

guessed_number = random.randint(1, 20)
print(guessed_number)

print("\t Guess a number from 1 to 20")

while True:
    try: 
        user_input = int(input("Enter a number: "))

        if user_input == guessed_number:
            print(f"You guessed correctly! The number was {guessed_number}")
            break

        elif user_input > guessed_number:
            print("your guessed number is high")

        elif  user_input < guessed_number:
            print("your guessed number is low")
        else:
            print("Invalid number")
    except ValueError:
        print("please enter valid number")
