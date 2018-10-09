def display_menu_get_choice():
    print('MAKE SELECTION FROM THE MENU')
    '''Display choices for user, return users' selection'''
    print('''
        Please type in the math operation you would like to complete:
        + for addition
        - for subtraction
        * for multiplication
        / for division
        q for quit
        ''')

    operation = input('Enter your selection: ')

    return operation

def addition(num1, num2):

    return num1 + num2

def substraction(num1, num2):

    return num1 - num2

def multiplication(num1, num2):

    return num1*num2

def division(num1, num2):

    # print('{} / {} = '.format(number_1, number_2))
    return num1 / num2

def message(msg):
    '''Display a message to the user'''
    print(msg)
