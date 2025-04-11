try :

    num1 = int(input("Enter a 1st number: "))
    num2 = int(input("Enter a 2nd number: "))
    num3 = int(input("Enter a 3rd number: "))

    if num1 > num2 and num1 > num3:
        print("1st number is largest")
    elif num2 > num1 and num2 > num3:
        print("2nd number is largest")
    elif num3 > num1 and num3 > num2:
        print("3rd number is largest")
    
except ValueError:
    print("Please enter a valid number!")
