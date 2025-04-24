user_input = input("Enter the traffic light color: ").lower()

if user_input == "red":
    print("STOP")

elif user_input == "green":
    print("GO")

elif user_input == "yellow":
    print("WAIT")

else:
    print("Invalid color")