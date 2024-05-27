print("1 = Addition")
print("2 = Multiplication")
print("3 = Subtraction")
print("4 = Division")
option = int(input("Choose an operation:"))
result=0
if (option in [1,2,3,4]):
    first= int(input("Enter the first number:"))
    second= int(input("Enter the second number:"))

    if (option == 1):
        result = first + second
    elif (option == 2):
        result = first * second
    elif (option == 3):
        result = first - second
    elif (option == 4):
        result = first // second
    
else:
    print("Invalid Operation entered")

print("The result of the operation is {}".format(result))
