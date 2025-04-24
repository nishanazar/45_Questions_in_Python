num1 = int(input("Enter a 1st number: "))
num2 = int(input("Enter a 2nd number: "))

operation   = input("Enter operation  [+ , -, *, /]: ")

if operation == "+":
    result = num1 + num2

elif operation == "-":
    result = num1 - num2

elif operation == "*":
    result = num1 * num2

elif operation == "/":
    if num2 != 0:
       result = num1 / num2 
    else:
        print("Division by 0 is not allowed!")
else:
    print("invalid number")
print(f"Result: {num1} {operation} {num2} = {result}")