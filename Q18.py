try:

    user_number:int = int(input("Enter a number: "))

    if user_number < 0 :
        print("Factorial is not defined for negative numbers.")
    else:
        find_factorial = 1
        for i in range(user_number, 1,-1):
            find_factorial *= i
        print(find_factorial)

except KeyboardInterrupt:
    print("\nSorry, process interrupted.")
except ValueError:
    print("please enter vaalid number")