# Importing libraries
# This code is made by Shourya Pant and Tejas Dwivedi

import math
import time

from tqdm import tqdm


def welcome():
    """
    Display a welcome message for the scientific calculator application.

    This function prints a decorative introduction to the calculator app,
    including the names and identifiers of the developers.

    Returns:
        None
    """
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
    for _ in tqdm(range(100), desc="Loading..."):
        time.sleep(0.02)
    print("----------------------------------------------------------")


def addition():
    """
    Perform the addition of n numbers provided by the user.

    This function prompts the user to enter how many numbers they want to add.
    It then collects the specified numbers from the user, allowing multiple
    entries for each number, and calculates the total sum.

    Returns:
        None
    """
    print("How many nums to add")
    number = int(input())
    total = 0
    for x in range(number):
        numbers_to_be_added = list(
            map(int, input(f"Enter number {x + 1}: ").split())
        )
        for y in numbers_to_be_added:
            total += y
    print("\n \n The sum of all numbers is : ", total, end="\n")


def subtraction():
    """
    Perform the subtraction of n numbers provided by the user.

    This function prompts the user to enter the total number of operands
    for subtraction. It handles different cases based on the number of
    operands.

    Returns:
        None
    """
    print("\n For how many variables you want to do subtraction?", end="\n")
    no_of_variable = int(input("\n Enter the total number of operands... "))
    if no_of_variable == 1:
        print(
            "\nInvalid operation. Please provide at least two operands to "
            "perform subtraction.",
            end="\n"
        )
    elif no_of_variable == 2:
        first_number = int(input("Enter first number:  "))
        second_number = int(input("Enter second number:  "))
        difference = first_number - second_number
        print(
            f"\n\nThe difference between {first_number} and {second_number} "
            f"is: {difference}",
            end="\n"
        )
    elif no_of_variable == 3:
        first_number = int(input("Enter first number:  "))
        second_number = int(input("Enter second number:  "))
        third_number = int(input("Enter third number:  "))
        difference = first_number - second_number - third_number
        print(
            f"\n\nThe difference between {first_number}, {second_number}, and "
            f"{third_number} is: {difference}",
            end="\n"
        )
    elif no_of_variable >= 4:
        numbers = []
        for x in range(no_of_variable):
            for _ in (input("Enter numbers: " + str(x + 1) + " ").split()):
                numbers.append(i)
            difference = int(numbers[0])
            for number in numbers[1:]:
                difference = difference - int(number)
        print(
            "\n\nThe difference between all the numbers is:", difference,
            end="\n\n"
        )


def multiplication():
    """
    Perform the multiplication of two or more numbers provided by the user.

    This function prompts the user to enter the total number of multiplicands
    for multiplication. It handles different cases based on the number of
    operands.

    Returns:
        None
    """
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
            number = float(input(
                "\nEnter the number which you want to multiply with itself: "
            ))
            result = number ** 2
            print(
                f"\n\nThe multiplication result of {number} with itself is: "
                f"{result}",
                end="\n\n"
            )
    elif choice == 2:
        first_number = float(input("\n Enter first number: "))
        second_number = float(input("\n Enter second number: "))
        result = first_number * second_number
        print(
            f"\n\nThe multiplication of {first_number} and {second_number} "
            f"is: {result}",
            end="\n\n"
        )
    elif choice >= 3:
        numbers = []
        for x in range(choice):
            for _ in (input("Enter numbers: " + str(x + 1) + " ").split()):
                numbers.append(i)
            result = 1
            for _ in numbers:
                result = result * float(x)
        print("\n \n The multiplication of numbers is: ", result, end="\n\n")


def division():
    """
    Perform the division of two numbers provided by the user.

    This function prompts the user to choose between performing division
    with integers or floating point numbers. It handles different cases based
    on the user's choice.

    Returns:
        None
    """
    print("\n 1. Do the division for the integers numbers ", end="\n")
    print("\n 2. Do the division for the floating point numbers ", end="\n")
    choice = int(input("\n Enter 1 or 2 "))
    if choice == 1:
        dividend = int(input("\n Enter the first number (Dividend): "))
        divisor = int(input("\n Enter the second Number (Divisor): "))
        if divisor == 0:
            print("\n Error!!!", end="\n")
            print(
                "\n\nThe division of a number by 0 is not possible",
                end="\n"
            )
        else:
            division = dividend / divisor
            print(
                f"\n\nThe division of {dividend} and {divisor} is: {division}",
                end="\n\n"
            )
    elif choice == 2:
        dividend = float(input("Enter the first number (Dividend): "))
        divisor = float(input("Enter the second number (Divisor): "))
        if divisor == 0:
            print("\n Error!!!", end="\n")
            print(
                "\n\nThe division of a number by 0 is not possible",
                end="\n\n"
            )
        else:
            division = dividend / divisor
            print(
                f"\n\nThe division between {dividend} and {divisor} is: "
                f"{division}",
                end="\n\n"
            )
    else:
        print("\n Error!!!! ..... \n", end="\n")
        print("Invalid choice please choose between 1 or 2", end="\n\n")


def modulus():
    """
    Calculate the modulus (remainder) of two numbers provided by the user.

    This function prompts the user to enter two numbers: the first number and
    the divisor. It calculates the modulus of the first number with respect to
    the divisor and displays the result.

    Returns:
        None
    """
    first_number = float(input("\n Enter  first number: "))
    divisor = float(input("\n Enter divisor: "))
    result = first_number % divisor
    print(
        f"\n\nThe modulus between {first_number} and {divisor} "
        f"is: {result:.2f}"
    )


def powers_exponents():
    """
    Calculate the power of a base number raised to a specified exponent.

    This function prompts the user to enter a base number and an exponent.
    It calculates the result of raising the base to the power of the exponent
    and displays the result.

    Returns:
        None
    """
    base = float(input("\nEnter the base number: "))
    exponent = float(input("\nEnter the exponent number: "))
    power = base ** exponent
    print(
        f"\n\nThe value of {base} to the power of {exponent} is: {power}",
        end="\n\n"
    )


def calculating_roots():
    """
    Calculate the roots of a number or the 1/nth power of a number.

    This function prompts the user to enter a number and the degree of the
    root they wish to calculate. It computes the nth root of the number using
    the formula and displays the result.

    Returns:
        None
    """
    number = float(input("\n Enter the number whose root you want to find: "))
    exponent = float(input("\n Which root you want? "))
    result = pow(number, 1 / exponent)
    if exponent == 2:
        print("\n The square root of ", number, "is: ", result, end="\n")
    elif exponent == 3:
        print("\n The cube root of ", number, "is: ", result, end="\n")
    else:
        print("\n The nth root of ", number, "is: ", result, end="\n")


def factorial():
    """
    Calculate the factorial of an integer.

    This function prompts the user to enter a number and calculates its
    factorial if the number is a non-negative integer. The factorial is
    computed by multiplying all positive integers up to the specified number.

    Returns:
        None
    """
    fact_value = 1
    number = float(input(
        "\nEnter a number whose factorial you want to calculate: "
    ))
    if number >= 1 and number.is_integer():
        for fact in range(1, int(number + 1)):
            fact_value *= fact
        print(
            f"\n\nThe factorial of the given number {number} is: {fact_value}",
            end="\n\n"
        )
    else:
        print("\n")
        for _ in tqdm(range(100), desc=" Error !!!!..."):
            time.sleep(0.01)
        print(
            "\nThe factorial cannot be calculated for negative numbers and "
            "decimal numbers!",
            end="\n\n"
        )


def trigonometry():
    """
    Calculate and display the result of a chosen trigonometric function.

    This function prompts the user to select a trigonometric function from
    a list of options (sin, cos, tan, sec, cosec, cot) and enter an angle
    in degrees. It converts the angle from degrees to radians and computes
    the result based on the selected function.

    Returns:
        int: Returns 0 upon completion of the function.
    """
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
    x = (x / 180) * math.pi
    match choice:
        case 1:
            print(math.sin(x), end="\n")
        case 2:
            print(math.cos(x), end="\n")
        case 3:
            print(math.tan(x), end="\n")
        case 4:
            print(1 / math.cos(x), end="\n")
        case 5:
            print(1 / math.sin(x), end="\n")
        case 6:
            print(1 / math.tan(x), end="\n")
        case _:
            print(
                "\n\nInvalid choice!!!!\n"
                "Please enter a valid choice (1-6)",
                end="\n "
            )

    return 0


def logarithms():
    """
    Calculate logarithmic values based on user input.

    This function prompts the user to choose between two types of logarithmic
    calculations.

    Returns:
        None
    """
    print("\n Which type of logarithms do you want to calculate?", end="\n")
    print("\n 1.  Natural logs, (Base=e or ln)", end="\n")
    print("\n 2. Logs with a base and value", end="\n")
    choice = int(input("\n Enter 1 or 2 "))
    if choice == 1:
        base = float(input(
            "\nEnter a base number whose log you want to calculate: "
        ))
        print(
            f"\n\nThe natural log of the number {base} is: "
            f"{math.log(base)}"
        )
    elif choice == 2:
        base = float(input(
            "\nEnter a base number whose log you want to calculate: "
        ))
        exponent = float(input(
            "\nEnter an exponent number which will be the log base: "
        ))
        print(
            f"\n\nThe log of {base} with log base {exponent} is: "
            f"{math.log(base, exponent)}",
            end="\n\n"
        )
    else:
        print("\n Print invalid choice!!!! \n\n")
        print("Enter a choice between 1 or 2 ")


def euclidean_distance():
    """
    Calculate the Euclidean distance between two points in a 2D space.

    This function prompts the user to enter the coordinates of two points
    (x1, y1) and (x2, y2). It calculates the Euclidean distance.

    Returns:
        None
    """
    x1 = float(input("\n Enter the x coordinate of the first point (x1): "))
    x2 = float(input("\n Enter the x coordinate of the second point (x2): "))
    y1 = float(input("\n Enter the y coordinate of the first point (y1): "))
    y2 = float(input("\n Enter the y coordinate of the second point (y2): "))
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    print(
        f"\n\nThe Euclidean distance between two points ({x1}, {y1}) "
        f"and ({x2}, {y2}) is: {distance}",
        end="\n\n"
    )


def area():
    """
    Calculate and display the area of various geometric figures.

    This function prompts the user to select a geometric figure from a list
    of options and then calculates the area based on the user's input.

    Returns:
        None
    """
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
    match choice:
        case 1:
            length = float(input("\n Enter The length of rectangle: "))
            breadth = float(input("\n Enter The breadth of rectangle: "))
            print("\n\n The area of rectangle is: ", length * breadth, end="\n")
        case 2:
            side = float(input("\n Enter The side of square: "))
            print("\n\n The area of square is : ", side * side, end="\n")
        case 3:
            height = float(input("\n Enter The height of triangle: "))
            breadth = float(input("\n Enter The breadth of triangle: "))
            print(
                f"\n\nThe area of the triangle is: {0.5 * height * breadth}",
                end="\n"
            )
        case 4:
            radius = float(input("\n Enter The radius of circle: "))
            print(
                f"\n\nThe area of the circle is: {math.pi * radius * radius:.4f}",
                end="\n"
            )
        case 5:
            no_of_sides = int(input(
                "\nEnter the number of sides of the regular polygon: "
            ))
            length = float(input("\n Enter length of side:"))
            ans = (length ** 2 * no_of_sides) / (
                    4 * math.tan(math.pi / no_of_sides)
            )
            print("{:.4f}".format(ans))
        case _:
            print(
                "\n\nInvalid choice!!! Please enter a valid choice (1-5)",
                end="\n"
            )


def calculator():
    """
    Display a calculator menu and perform the selected mathematical operation.

    This function presents a menu of various mathematical operations that
    the user can choose.

    Returns:
        None
    """
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

    choice = int(input("Please Enter a Choice(1-12) what you want to do??"))

    match choice:
        case 1:
            addition()
        case 2:
            subtraction()
        case 3:
            multiplication()
        case 4:
            division()
        case 5:
            modulus()
        case 6:
            powers_exponents()
        case 7:
            calculating_roots()
        case 8:
            factorial()
        case 9:
            trigonometry()
        case 10:
            logarithms()
        case 11:
            euclidean_distance()
        case 12:
            area()
        case _:
            print("\n\nInvalid choice !!!!!! ", end="\n")
            print("\nPlease enter a valid choice (1-12) ", end="\n\n")


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
        yes_no = input("\n Do you want to continue (Yes or No) ?")
        if yes_no in ["Y", "y", "Yes", "yes"]:
            calculator()
        else:
            break
