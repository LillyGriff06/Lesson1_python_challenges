#Python programming challenges

#Area of a triangle
def triangleArea():
    base = float(input("Input base of the triangle:  "))
    height = float(input("Input height of the triangle:  "))
    triArea = (base * height) / 2
    print("The area of the triangle with a base of", base, "and a height of", height, "is", triArea)

#Power calculator
def powerCalculator():
    voltage = float(input("Input the voltage:  "))
    current = float(input("Input the current:  "))
    power = voltage * current
    print("The power calculated from a voltage of", voltage, "and a current of", current, "is", power)

#Return the sum of two numbers
def sumTwoNumbers():
    num1 = int(input("Input a number:  "))
    num2 = int(input("Input another number:  "))
    addition = num1 + num2
    print("The sum of the two numbers", num1, "and", num2, "is", addition)



#Menu
def menu():
    print("1. Area of a triangle")
    print("2. Power calculator")
    print("3. Sum of two numbers")
    print("7. Exit")
    option = int(input("Choose an option:  "))
    while option >= 1 and option < 7:
        if option == 1:
            triangleArea()
            option = int(input("Choose an option:  "))
        if option == 2:
            powerCalculator()
            option = int(input("Choose an option:  "))
        if option == 3:
            sumTwoNumbers()
            option = int(input("Choose an option:  "))
menu()
            
        
