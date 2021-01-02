"""
Author: Keval Varia
File: Discrepancy Calculator
Purpose: to calculate percent discrepancy and percent difference (mostly for physics)
"""

'''
function: percent_discrepancy():
description: calculate the percent discrepancy between a measured value and an expecte value
return: double
'''
def percent_discrepancy(measured, expected):
    result = abs(measured - expected) / expected
    result *= 100
    return result


'''
function: percent_difference():
description: calculate the percent difference between a measured value and an expecte value
return: double
'''
def percent_difference(x1, x2):
    avg = (x1 + x2 / 2)
    result = abs(x1 - x2) / avg
    result *= 100
    return result


'''
function: menu()
description: print the main menu to the console
return: void
'''
def menu():
    print("Menu:")
    print("1. Percent Discrepancy")
    print("2. Percent Difference")
    print("0. Exit")


'''
function: main():
description:
- print the main menu
- allow the user to select an option
- perform calculation based on appropriate input
- print the output
- return to main menu (unless exit is triggered)
return: void
'''
def main():
    while True:
        menu()
        choice = int(input("Enter selection: "))
        print()

        if choice == 0:
            print("Bye!")
            break
        elif choice == 1:
            measured = float(input("Experimental = "))
            expected = float(input("Known = "))
            result = percent_discrepancy(measured, expected)
            print(" - Percent Discrepancy: " + str(result))
        elif choice == 2:
            measured = float(input("Experimental = "))
            expected = float(input("Known = "))
            result = percent_discrepancy(measured, expected)
            print(" - Percent Difference: " + str(result))
        else:
            print("Invalid input. Try again")
        print()

if __name__ == '__main__':
    main()