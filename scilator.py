import math
import time
divisor = 10 # number to divide by to get coefficient between 0 and 10
exponent = 1 # exponent for the scientific notation
Running = True # boolean for the main loop
conversion_mode = 0 # variable for the type of conversion

def isfloat(value): # function to check if the input can be converted to a float
    try:
        float(value)
        return True
    except ValueError:
        return False

def isNegative(value): # function to check if the input is negative
    try:
       math.sqrt(value)
       return False
    except ValueError:
       return True

def reset(): # function to reset the variables
    coefficient = 0
    exponent = 1
    divisor = 10
    conversion_mode = 0
    end_time1 = 0
    end_time = 0
    start_time = 0

# coefficient * 10(base) ^ exponent

while Running: # main loop
    input_type = input('Enter 1 for standard to scientific, 2 for scientific to standard, and 3 to exit: ') # input for the type of conversion
    if isfloat(input_type): # check if the input can be converted to a float
     if float(input_type) == 1: # check if the input is 1
         conversion_mode = 1
     elif float(input_type) == 2: # check if the input is 2
         conversion_mode = 2
     elif float(input_type) == 3: # check if the input is 3
      Running = False # exiting the program
      break
    else:
        print('Please enter a valid input \n')


    while conversion_mode == 2: # scientific to standard

        # getting inputs
     coeff = input('Enter the coefficient: ')
     expon = input('Enter the exponent: ')

     if isfloat(coeff) and isfloat(expon): # both inputs must be floats to continue
        start_time = time.time() # start timer

        # testing for overflow
        try:
            round((float(coeff) * 10 ** float(expon)), 5 )
        except OverflowError:
            print('Overflow error, try again \n')
            conversion_mode = 0
            break
        else:
         end_time1 = time.time() # end timer
         print(round((float(coeff) * 10 ** float(expon)), 5 )) # printing the final answer rounded to 5 d.p.
         print(round(((end_time1 - start_time)*1000000), 2 ), 'ms \n') # printing the time taken in rounded ms
         reset()

     else:
        print('Please enter a valid input \n')
        reset()
        break

     reset()
     break



    while conversion_mode == 1: # standard to scientific
        x = input('Enter the number in standard form: ') # input for the number in standard form

        if isfloat(x):  # Check if the input can be converted to a float
                start_time = time.time() # start timer
                floatput = abs(float(x.replace(',', '')))  # Removing commas and converting to a positive float
                coefficient = floatput / divisor  # find coefficient

                if coefficient > 1: # Checking if the coefficient is greater than 1

                    while coefficient > 10.0: # loop until under 10
                        divisor *= 10
                        exponent += 1

                        try: # testing for overflow
                            coefficient = floatput / divisor
                        except OverflowError:
                            print('Overflow error, try again \n')
                            reset()
                            break

                elif coefficient < 1:

                    while coefficient < 1.0: # loop until over 1
                        divisor /= 10
                        exponent -= 1
                        coefficient = floatput / divisor

                if isNegative(float(x)):
                    end_time = time.time() # end timer
                    print('-', round(coefficient, 5), 'x 10 ^', round(exponent, 5)) # printing negative final answer, rounded to 5 d.p.
                    print(round(((end_time - start_time)*1000000), 2), 'ms \n') # printing the time taken
                    reset()
                    break

                end_time = time.time() # end timer
                print(round(coefficient, 5), 'x 10 ^', round(exponent, 5))  # Printing the coefficient and exponent final answer rounded to 5 d.p.
                print(round(((end_time - start_time)*1000000), 2), 'ms \n') # printing the time taken in rounded ms
                reset()
                break

        else:
            print('Please enter a valid numeric input \n')
            conversion_mode = 0 # Resetting the conversion type
            break