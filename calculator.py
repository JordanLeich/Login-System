# Code created by Jordan Leich on 6/11/2020, email me at jordanleich@gmail.com if you wish to code together!

# Imports
import end
from colored import fg, attr

# Global Variables
green = fg('green')
red = fg('red')
reset = attr('reset')


def restart():
    user_restart = input(str('Do you wish to use the calculator again (yes or no) '))
    print()

    if user_restart.lower() == 'y' or user_restart.lower() == 'yes':
        calculator()

    elif user_restart.lower() == 'n' or user_restart.lower() == 'no':
        program_choice = input(str('Would you like to use another program from the login system page (yes or no) '))
        print()

        if program_choice.lower() == 'y' or program_choice.lower() == 'yes':
            from loginsystem import logged_in
            logged_in()

        elif program_choice.lower() == 'n' or program_choice.lower() == 'no':
            end.end()

        else:
            print(red + 'User input error found! restarting user choice...\n' + reset)
            restart()

    else:
        print(red + 'User input error found! restarting user choice...\n' + reset)
        restart()


def calculator():
    first_number = int(input("Enter first number: "))
    print()

    operator = input(str("Enter an operation (+ | - | * | /): "))
    print()

    second_number = int(input("Enter second number: "))
    print()

    if operator == '+':
        print(green, first_number + second_number, reset, '\n')
        restart()

    elif operator == '-':
        print(green, first_number - second_number, reset, '\n')
        restart()

    elif operator == '*':
        print(green, first_number * int(second_number), reset, '\n')
        restart()

    elif operator == '/':
        print(green, first_number / second_number, reset, '\n')
        restart()

    else:
        print(red, 'Unknown Operator! Restarting Calculator...\n', reset)
        calculator()


calculator()
