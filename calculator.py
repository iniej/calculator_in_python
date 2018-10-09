import ui


def handle_operations(operation):

    if operation == "+":
        number_1 = int(input('Please enter the first number: '))
        number_2 = int(input('Please enter the second number: '))
        result = ui.addition(number_1, number_2)
        print(result)

    elif operation == "-":
        number_1 = int(input('Please enter the first number: '))
        number_2 = int(input('Please enter the second number: '))
        result = ui.substraction(number_1, number_2)
        print(result)

    elif operation == "*":
        number_1 = int(input('Please enter the first number: '))
        number_2 = int(input('Please enter the second number: '))
        result = ui.multiplication(number_1, number_2)
        print(result)

    elif operation == "/":
        number_1 = int(input('Please enter the first number: '))
        number_2 = int(input('Please enter the second number: '))
        while number_2 == 0:
            try:
                print('Please enter a valid number')
                number_2 = int(input('Please enter the second number: '))
                print(' ')
            except:
                print('Bad input')
                print(' ')

        result = ui.division(number_1, number_2)
        print(result)

    elif operation == 'q' or operation == 'Q':
        print('Bye!')
        quit()

    else:
        ui.message('Please enter a valid selection\n')


def main():

    quit = 'q'
    operation = None

    while operation != quit:
        operation = ui.display_menu_get_choice()
        handle_operations(operation)


if __name__ == '__main__':
    main()
