import time

divisor = 10  # number to divide by to get coefficient between 0 and 10
exponent = 1  # exponent for the scientific notation
Running = True  # boolean for the main loop
conversion_mode = 0  # variable for the type of conversion
coefficient = 0  # Define coefficient as a global variable
start_time = 0  # Define start_time as a global variable

def isfloat(value):  # function to check if the input can be converted to a float
    try:
        float(value)
        return True
    except ValueError:
        return False

def isNegative(value):  # function to check if the input is negative
    if value < 0:
        return True
    else:
        return False

def isint(value):  # function to check if the input can be converted to an int
    try:
        int(value)
        return True
    except ValueError:
        return False

def reset():  # function to reset the variables
    global coefficient, exponent, divisor, conversion_mode, start_time
    coefficient = 0
    exponent = 1
    divisor = 10
    conversion_mode = 0
    start_time = 0

while Running:  # main loop
    input_type = input('Enter 1 for standard to scientific, 2 for scientific to standard, and 3 to exit: ')  # input for the type of conversion

    if isint(input_type):  # check if the input can be converted to a float
        conversion_mode = int(input_type)
    else:
        print('Please enter a valid input \n')

    while conversion_mode == 1:  # standard to scientific
        x = input('Enter the number in standard form: ')  # input for the number in standard form

        if isfloat(x):  # Check if the input can be converted to a float
            start_time = time.time()  # start timer
            floatput = abs(float(x.replace(',', '')))  # Removing commas and converting to a positive float
            coefficient = floatput / divisor  # find coefficient

            if coefficient > 1:  # Checking if the coefficient is greater than 1

                while coefficient > 10.0:  # loop until under 10
                    divisor *= 10
                    exponent += 1

                    try:  # testing for overflow
                        coefficient = floatput / divisor
                    except OverflowError:
                        print('Overflow error, try again \n')
                        reset()
                        break

            elif coefficient < 1:

                while coefficient < 1.0:  # loop until over 1
                    divisor /= 10
                    exponent -= 1
                    coefficient = floatput / divisor

            if isNegative(float(x)):
                end_time_conv_1 = time.time()  # end timer
                print(f'-{round(coefficient, 5)}x10^{round(exponent, 5)}')  # printing negative final answer, rounded to 5 d.p.
                print(f'{round(((end_time_conv_1 - start_time) * 1000000), 2)} ms \n')  # Printing time taken in rounded ms
                reset()
                break
            else:
                end_time_conv_1 = time.time()  # end timer
                print(f'{round(coefficient, 5)}x10^{round(exponent, 5)}')  # Printing the coefficient and exponent final answer rounded to 5 d.p.
                print(f'{round(((end_time_conv_1 - start_time) * 1000000), 2)} ms \n')  # Printing time taken in rounded ms
                reset()
                break

        else:
            print('Please enter a valid numeric input \n')
            reset()
            break

    while conversion_mode == 2:  # scientific to standard

        print('coefficient x 10 ^ exponent')

        # getting inputs
        stroefficient = input('Enter the coefficient: ')
        strexponent = input('Enter the exponent: ')

        if isfloat(stroefficient) and isfloat(strexponent):  # both inputs must be floats to continue
            coefficient = float(stroefficient)
            exponent = float(strexponent)
            start_time = time.time()  # start timer

            # testing for overflow
            try:
                coefficient * 10 ** exponent  # type: ignore
            except OverflowError:
                print('Overflow error, try again \n')
                break
            else:
                end_time_conv_2 = time.time()  # end timer
                print(round((coefficient * 10 ** exponent), 5))  # printing the final answer rounded to 5 d.p.
                print(f'{round((end_time_conv_2 - start_time) * 1000000, 2)} ms \n')  # printing the time taken in rounded ms
                reset()

        else:
            print('Please enter a valid input \n')
            reset()
            break

    if conversion_mode == 3:  # exit
        exit()
