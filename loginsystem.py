# Created by Jordan Leich on 7/19/2020

# Imports
from colored import fg, attr
import end
import restart

# Global variables
green = fg('green')
red = fg('red')
reset = attr('reset')
existing_users1 = ['test@gmail.com', 'test123']


def logged_in():
    print(green + 'Congrats, you have successfully logged in!\n' + reset)

    user_choice2 = input(str('You have access to our Math Calculator, Anti-Virus Program, or Junk File Cleaner (calc, '
                             'antivirus, junk, or quit): '))

    if user_choice2.lower() == 'c' or user_choice2.lower() == 'calc' or user_choice2.lower() == 'calculator':
        calculator.calculator()

    elif user_choice2.lower() == 'a' or user_choice2.lower() == 'anti' or user_choice2.lower() == 'antivirus':
        antivirus.antivirus()

    elif user_choice2.lower() == 'j' or user_choice2.lower() == 'junk' or user_choice2.lower() == 'clean':
        cleaner.cleaner()

    elif user_choice2.lower() == 'q' or user_choice2.lower() == 'quit':
        end.end()

    else:
        print(red + 'User input error found! Restarting input...' + reset)
        logged_in()


def new_account():
    new_name = input(str('Please enter your first name: '))
    print()

    print('Hi there,', new_name + '!\n')

    new_email = input(str('Please enter a valid email address to sign up with: '))
    print()

    if '@' not in new_email.lower():
        print(
            red + 'Error found... A valid email address must include an @ symbol! Restarting sign up page...\n' + reset)
        new_account()

    new_password = input('Please enter a new password to sign up with: ')
    print()
    confirm_password = input('Retype your new password for confirmation: ')
    print()

    if new_password == confirm_password:
        logged_in()

    elif new_password != confirm_password:
        print(red + 'Your passwords do not match up correctly! Restarting sign up page...\n' + reset)

    else:
        print(red + 'Error found! Restarting sign up page...\n' + reset)
        new_account()


def start():
    print(green + 'Welcome to the login system!\n' + reset)
    first_login = input(str('Are you an existing user (yes or no) '))
    print()

    if first_login.lower() == 'y' or first_login.lower() == 'yes':
        existing_email = input(str('Enter an existing email address: '))
        print()

        if existing_email not in existing_users1:
            invalid_email = input(red + 'The email address you provided does not exist!' + reset + ' Would you like to '
                                                                                                   'create a new '
                                                                                                   'account (yes or '
                                                                                                   'no) ')
            print()

            if invalid_email.lower() == 'y' or invalid_email.lower() == 'yes':
                new_account()

            elif invalid_email.lower() == 'n' or invalid_email.lower() == 'no':
                restart.restart()

            else:
                print('Error found with user input...')
                restart.restart()

        existing_password = input('Enter an existing password for this account: ')
        print()

        if existing_email and existing_password in existing_users1:
            logged_in()

        elif existing_email not in existing_users1 and existing_password in existing_users1:
            invalid_email = input(red + 'The email address you provided does not exist!' + reset + ' Would you like to '
                                                                                                   'create a new '
                                                                                                   'account (yes or '
                                                                                                   'no) ')
            print()

            if invalid_email.lower() == 'y' or invalid_email.lower() == 'yes':
                new_account()

            elif invalid_email.lower() == 'n' or invalid_email.lower() == 'no':
                restart.restart()

            else:
                print('Error found with user input...')
                restart.restart()

        elif existing_password not in existing_users1:
            invalid_password = input(red + 'The password you provided does not exist!' + reset + ' Would you like to '
                                                                                                 'create a new '
                                                                                                 'account (yes or '
                                                                                                 'no) ')
            print()

            if invalid_password.lower() == 'y' or invalid_password.lower() == 'yes':
                new_account()

            elif invalid_password.lower() == 'n' or invalid_password.lower() == 'no':
                restart.restart()

            else:
                print('Error found with user input...')
                restart.restart()

    elif first_login.lower() == 'n' or first_login.lower() == 'no':
        user_choice1 = input(str('Would you like to create a new account (yes or no): '))
        print()

        if user_choice1.lower() == 'y' or user_choice1.lower() == 'yes':
            new_account()

        elif user_choice1.lower() == 'n' or user_choice1.lower() == 'no':
            end.end()

        else:
            print(red + 'User input error found!\n' + reset)
            restart.restart()

    else:
        print(red + 'User input error found!\n' + reset)
        restart.restart()


start()
