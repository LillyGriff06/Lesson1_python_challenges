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
    if num1%7==0 or num2%7==0:
        division = num1 / num2
        print("The answer is" , division)
    elif num1%11==0 or num2%11==0:
        multiplication = num1 * num2
        print("The answer is", multiplication)
    else:
        addition = num1 + num2
        print("The sum of the two numbers", num1, "and", num2, "is", addition)

#Convert age to days
def age_to_days():
    age = int(input("Input age:  "))
    while age < 0:
        age = int(input("Input age:  "))
    age_in_days = (age * 365) + (age // 4)
    print("The age", age, "in days is", age_in_days)

#Encode Morse
def encode_morse():
    char_to_dots = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
        ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
        '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }

    code = input("Input data to encode:  ")
    code = code.upper()
    encoded = ""
    length = len(code)
    for x in range(1, length+1):
      encoded += char_to_dots[code[x-1]]
    print("The data", code, "becomes", encoded)
    
#Calculate the profit
def profitCalculator():
    profit={
        "cost_price":32.67,
        "sell_price":45.00,
        "inventory":1200
        }
    totalCost = profit["cost_price"] * profit["inventory"]
    totalSell = profit["sell_price"] * profit["inventory"]
    totalProfit = totalSell - totalCost
    print("The cost price is", profit["cost_price"])
    print("The sell price is", profit["sell_price"])
    print("The inventory is", profit["inventory"])
    print("The total profit is", totalProfit)


#Menu
def menu():
    print("1. Area of a triangle")
    print("2. Power calculator")
    print("3. Sum of two numbers")
    print("4. Convert age to days")
    print("5. Encode morse")
    print("6. Calculate the profit")
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
        if option == 4:
            age_to_days()
            option = int(input("Choose an option:  "))
        if option == 5:
            encode_morse()
            option = int(input("Choose an option:  "))
        if option == 6:
            profitCalculator()
            option = int(input("Choose an option:  "))
menu()
            
        
