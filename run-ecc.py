import ecc

def enterNumber(text):
    number = input(text)
    if(number.isdigit()):
        return int(number)
    else:
        raise ValueError('Please enter a number!')

def printMenu():
    choice = None
    while(choice == None or choice > 2 or choice < 0):
        print('\n0: Exit\n1: Show all points in the curve\n2: Calculate multiplies')
        choice = enterNumber('Make your choice: ')

    return choice

## Starting point for the application ##
try:
    print('ECC Calculator')
    print('--------------')
    print('Created in 2013 by Benjamin Mestdagh\n')
   
    a = enterNumber('Enter a: ')
    b = enterNumber('Enter b: ')
    p = enterNumber('Enter p: ')
    calculator = ecc.EccCalculator(a,b,p)

    choice = printMenu()

    while(choice > 0):
        if(choice == 1):
            print('\nAll points in the curve (a={}, b={}, p={}):'.format(a,b,p))
            results = calculator.calculateAllPoints()
            for point in results:
                print('({},{})'.format(point.x, point.y))
        else:
            n = enterNumber('Enter n: ')
            x = enterNumber('Enter x: ')
            y = enterNumber('Enter y: ')
       
            try:
                print('\nThe multiplies:')
                print('\n'.join(calculator.calculateG(n, x, y)))
            except ValueError as e:
                print(e)

        choice = printMenu()
    else:
        print('Bye!')

except ValueError as e:
    print(e)
