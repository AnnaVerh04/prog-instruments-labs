# IMPORTING LIABRARIES
# THIS CODE IS MADE BY SHOURYA PANT AND TEJAS DWIVEDI

import math
import time

from tqdm import tqdm


# This function is designed for the INTRODUCTION TO OUR CALCULATOR PROGRAM

def welcome():
    print(
        "\n\n---------------------------------------------------------",
        end=""
    )
    print(
        "\n|\n|  Welcome to the scientific Calculator app .....  \t|",
        end="\n"
    )
    print(
        "|\n| Made by:", "Shourya pant(0105CS191109) \t\t|",
        end="\n"
    )
    print("|\n| \t       and  \t\t\t \t\t|")
    print(
        "|\n| \t     Tejas dwivedi(0105CS191123) \t\t|",
        end="\n\n"
    )
    for i in tqdm(range(100), desc="Loading..."):
        time.sleep(0.02)
    print("----------------------------------------------------------")


# This function is designed for performing the ADDITION OF n numbers

def addition():
    print("How many nums to add")
    number = int(input())
    sum = 0
    for x in range(number):
        numbers_to_be_added = list(
            map(int, input(f"Enter number {x + 1}: ").split())
        )
        for y in numbers_to_be_added:
            sum += y
    print("\n \n The sum of all numbers is : ", sum, end="\n")


# This function is designed for performing the SUBTRACTION of n numbers

def subtraction():
    print("\n For how many variables you want to do subtraction?", end="\n")
    No_of_variable = int(input("\n Enter the total number of operands... "))
    if No_of_variable == 1:
        print(
            "\nInvalid operation. Please provide at least two operands to "
            "perform subtraction.",
            end="\n"
        )
    elif No_of_variable == 2:
        Num1 = int(input("Enter first number:  "))
        Num2 = int(input("Enter second number:  "))
        difference = Num1 - Num2
        print(
            f"\n\nThe difference between {Num1} and {Num2} is: {difference}",
            end="\n"
        )
    elif No_of_variable == 3:
        Num1 = int(input("Enter first number:  "))
        Num2 = int(input("Enter second number:  "))
        Num3 = int(input("Enter third number:  "))
        difference = Num1 - Num2 - Num3
        print(
            f"\n\nThe difference between {Num1}, {Num2}, and {Num3} is: "
            f"{difference}",
            end="\n"
        )
    elif No_of_variable >= 4:
        numbers = []
        for x in range(No_of_variable):
            for i in (input("Enter numbers: " + str(x + 1) + " ").split()):
                numbers.append(i)
            difference = int(numbers[0])
            for number in numbers[1:]:
                difference = difference - int(number)
        print(
            "\n\nThe difference between all the numbers is:", difference,
            end="\n\n"
        )


# This function is designed to perform MULTIPLICATION of two or more numbers

def multiplication():
    print("\n How many numbers do you want to get multiply ???", end="\n")
    choice = int(input("\n Enter total number of multiplicands:"))
    if choice == 1:
        print(
            "\nError: Multiplication of one number is not possible",
            end="\n"
        )
        print(
            "\nDo you wish to multiply that number with itself?",
            end="\n"
        )
        option = str(input("Yes or NO , enter (Y,N): "))
        if option == 'y' or option == "Y":
            Number = float(input(
                "\nEnter the number which you want to multiply with itself: "
            ))
            result = Number ** 2
            print(
                f"\n\nThe multiplication result of {Number} with itself is: "
                f"{result}",
                end="\n\n"
            )
    elif choice == 2:
        Number1 = float(input("\n Enter first number: "))
        Number2 = float(input("\n Enter second number: "))
        result = Number1 * Number2
        print(
            f"\n\nThe multiplication of {Number1} and {Number2} is: {result}",
            end="\n\n"
        )
    elif choice >= 3:
        numbers = []
        for x in range(choice):
            for i in (input("Enter numbers: " + str(x + 1) + " ").split()):
                numbers.append(i)
            result = 1
            for x in numbers:
                result = result * float(x)
        print("\n \n The multiplication of numbers is: ", result, end="\n\n")


# This function is designed to perform DIVISION of two numbers

def division():
    print("\n 1. Do the division for the integers numbers ", end="\n")
    print("\n 2. Do the division for the floating point numbers ", end="\n")
    choice = int(input("\n Enter 1 or 2 "))
    if choice == 1:
        Num1 = int(input("\n Enter the first number (Dividend): "))
        Num2 = int(input("\n Enter the Second NUmber (Divisor): "))
        if Num2 == 0:
            print("\n Error!!!", end="\n")
            print(
                "\n\nThe division of a number by 0 is not possible",
                end="\n"
            )
        else:
            Division = Num1 / Num2
            print(
                f"\n\nThe division of {Num1} and {Num2} is: {Division}",
                end="\n\n"
            )
    elif choice == 2:
        Num1 = float(input("Enter the first number (Dividend): "))
        Num2 = float(input("Enter the second number (Divisor): "))
        if Num2 == 0:
            print("\n ERROR!!!", end="\n")
            print(
                "\n\nThe division of a number by 0 is not possible",
                end="\n\n"
            )
        else:
            Division = Num1 / Num2
            print(
                f"\n\nThe division between {Num1} and {Num2} is: "
                f"{Division}",
                end="\n\n"
            )
    else:
        print("\n Error!!!! ..... \n", end="\n")
        print("Invalid choice please choose between 1 or 2", end="\n\n")


# This funciton is designed for CALCULATING THE MODULUS OF the numbers

def modulus():
    x = float(input("\n Enter  first number: "))
    y = float(input("\n Enter divisor: "))
    modulus = x % y
    print(
        f"\n\nThe modulus between {x} and {y} is: {modulus:.2f}"
    )


# This function is designed for CALCULATING THE POWERS taking BASE AND  EXPONENTIAL  values from the user

def powers_exponents():
    Base = float(input("\nEnter the base number: "))
    exponent = float(input("\nEnter the exponent number: "))
    power = Base ** exponent
    print(
        f"\n\nThe value of {Base} to the power of {exponent} is: {power}",
        end="\n\n"
    )


# This function is designed to CALCULATE THE ROOTS OF A NUMBER OR 1/NTH POWER OF A NUMBER

def calculating_roots():
    Number = float(input("\n Enter the number whose root you want to find: "))
    exponent = float(input("\n Which root you want? "))
    result = pow(Number, 1 / exponent)
    if exponent == 2:
        print("\n The square root of ", Number, "is: ", result, end="\n")
    elif exponent == 3:
        print("\n The cube root of ", Number, "is: ", result, end="\n")
    else:
        print("\n The nth root of ", Number, "is: ", result, end="\n")


# This function is designed to calculate the FACTORIAL OF A NUMBER

def factorial():
    factorial = 1
    Number = float(input(
        "\nEnter a number whose factorial you want to calculate: "
    ))
    if (Number >= 1) and Number.is_integer() == True:
        for fact in range(1, int(Number + 1)):
            factorial = factorial * fact
        print(
            f"\n\nThe factorial of the given number {Number} is: {factorial}",
            end="\n\n"
        )
    else:
        print("\n")
        for i in tqdm(range(100), desc=" Error !!!!..."):
            time.sleep(0.01)
        print(
            "\nThe factorial cannot be calculated for negative numbers and "
            "decimal numbers!",
            end="\n\n"
        )


# This function is designed to calculate the TRIGNOMETRY

def trigonometry():
    print(
        "\nWhich trigonometric function do you want to use\n"
        "1. Sin\n"
        "2. Cos\n"
        "3. Tan\n"
        "4. Sec\n"
        "5. Cosec\n"
        "6. Cot",
        end="\n"
    )

    choice = float(input("\n Enter choice (1-6): "))
    x = float(input("\n Enter the values in degrees: "))
    x = (x / 180) * 3.14159265359
    if (choice == 1):
        print(math.sin(x), end="\n")
    elif (choice == 2):
        print(math.cos(x), end="\n")
    elif (choice == 3):
        print(math.tan(x), end="\n")
    elif (choice == 4):
        print(1 / math.cos(x), end="\n")
    elif (choice == 5):
        print(1 / math.sin(x), end="\n")
    elif (choice == 6):
        print(1 / math.tan(x), end="\n")
    else:
        print(
            "\n\nInvalid choice!!!!\n"
            "Please enter a valid choice (1-6)",
            end="\n "
        )
    return (0)


# This function  is designed for calculating the LOGARITHMIC VALUES

def logarithms():
    print("\n Which type of logarithms do you want to calculate?", end="\n")
    print("\n 1.  Natural logs, (Base=e or ln)", end="\n")
    print("\n 2. Logs with a base and value", end="\n")
    choice = int(input("\n Enter 1 or 2 "))
    if choice == 1:
        Base = float(input(
            "\nEnter a base number whose log you want to calculate: "
        ))
        print(
            f"\n\nThe natural log of the number {Base} is: "
            f"{math.log(Base)}"
        )
    elif choice == 2:
        Base = float(input(
            "\nEnter a base number whose log you want to calculate: "
        ))
        Exponent = float(input(
            "\nEnter an exponent number which will be the log base: "
        ))
        print(
            f"\n\nThe log of {Base} with log base {Exponent} is: "
            f"{math.log(Base, Exponent)}",
            end="\n\n"
        )
    else:
        print("\n Print invalid choice!!!! \n\n")
        print("Enter a choice between 1 or 2 ")


# This function  is designed for calculating the EUCLEDIAN DISTANCE BETWEEN TWO POINTS

def euclidean_distance():
    x1 = float(input("\n Enter the x coordinate of the first point (x1): "))
    x2 = float(input("\n Enter the x coordinate of the second point (x2): "))
    y1 = float(input("\n Enter the y coordinate of the first point (y1): "))
    y2 = float(input("\n Enter the y coordinate of the second point (y2): "))
    Eucledian_distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print(
        f"\n\nThe Euclidean distance between two points ({x1}, {y1}) "
        f"and ({x2}, {y2}) is: {Eucledian_distance}",
        end="\n\n"
    )


# This function is designed to CALCULATE AREA OF DIFFERENT POLYGONS

def area():
    print(
        "\nWhich figure area do you want to calculate?\n"
        "1. Rectangle\n"
        "2. Square\n"
        "3. Triangle\n"
        "4. Circle\n"
        "5. Regular polygon",
        end="\n"
    )
    choice = int(input("\n Enter a choice (1-5)"))
    if choice == 1:
        length = float(input("\n Enter The length of rectangle: "))
        breadth = float(input("\n Enter The breadth of rectangle: "))
        print("\n\n The area of rectangle is: ", length * breadth, end="\n")
    elif choice == 2:
        side = float(input("\n Enter The side of square: "))
        print("\n\n The area of square is : ", side * side, end="\n")
    elif choice == 3:
        height = float(input("\n Enter The height of triangle: "))
        breadth = float(input("\n Enter The breadth of triangle: "))
        print(
            f"\n\nThe area of the rectangle is: {height * breadth}",
            end="\n"
        )
    elif choice == 4:
        Radius = float(input("\n Enter The radius of circle: "))
        print(
            f"\n\nThe area of the circle is: {math.pi * Radius * Radius:.4f}",
            end="\n"
        )
    elif choice == 5:
        no_of_sides = int(input(
            "\nEnter the number of sides of the regular polygon: "
        ))
        length = float(input("\n Enter length of side:"))
        ans = (length ** 2 * no_of_sides) / (
                4 * math.tan(math.pi / no_of_sides)
        )
        print("{:.4f}".format(ans))
    else:
        print(
            "\n\nInvalid choice!!! Please enter a valid choice (1-5)",
            end="\n"
        )


#  THE MAIN MENU

def calculator():
    welcome()
    print("\n What do you want to do with our calculator?", end="\n")
    print("\n Main menu: ", end="\n\n")
    print("\n1. Adding two or more numbers", end="\n")
    print("\n2. Subtracting two or more numbers", end="\n")
    print("\n3. Multiplying two or more numbers", end="\n")
    print("\n4. Dividing numbers", end="\n")
    print("\n5. Taking modulus (remainder) of numbers", end="\n")
    print("\n6. Calculating powers or exponents", end="\n")
    print("\n7. Calculating roots or 1/nth powers of a number", end="\n")
    print("\n8. Calculating the factorial", end="\n")
    print("\n9. Trigonometry", end="\n")
    print("\n10. Calculating logarithms and natural logs", end="\n")
    print(
        "\n11. Calculating euclidean distance between two points",
        end="\n"
    )
    print(
        "\n12. Calculating area of various shapes and polygons",
        end="\n"
    )
    print("\n\n Please enter a valid choice (1-12) ", end="\n\n")
    choice = int(input("Please Enter a Choice(1-12) what you want to do??"))

    if choice == 1:
        addition()
    elif choice == 2:
        subtraction()
    elif choice == 3:
        multiplication()
    elif choice == 4:
        division()
    elif choice == 5:
        modulus()
    elif choice == 6:
        powers_exponents()
    elif choice == 7:
        calculating_roots()
    elif choice == 8:
        factorial()
    elif choice == 9:
        trigonometry()
    elif choice == 10:
        logarithms()
    elif choice == 11:
        euclidean_distance()
    elif choice == 12:
        area()
    else:
        print("\n\n Invalid choice !!!!!! ", end="\n")
        print("\n \n Please enter a valid choice (1-12) ", end="\n\n")


# THE MAIN FUNCITON

if __name__ == "__main__":

    print(
        "\n\n Hello everyone welcome to our calculator program .........",
        end="\n"
    )
    print("\n")
    for i in tqdm(range(100), desc=" Initializing..."):
        time.sleep(0.01)
    calculator()

    while True:
        Yes_no = input("\n Do you want to continue (Yes or No) ?")
        if Yes_no in ["Y", "y", "Yes", "yes"]:
            calculator()
        else:
            break
