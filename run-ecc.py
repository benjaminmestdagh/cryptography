import ecc

def enterNumber(text):
    number = input(text)
    try:
        return int(number)
    except:
        raise ValueError('Please enter a number!')

def printMenu():
    choice = None
    while(choice == None or choice > 4 or choice < 0):
        print("\n0: Exit"
              "\n1: Show all points in the curve"
              "\n2: Calculate multiples"
              "\n3: Addition of two points"
              "\n4: Subtraction of two points")
        choice = enterNumber('Make your choice: ')

    return choice

def doAdditionOrSubtraction(subtraction = False):
    x1 = enterNumber('Enter first x: ')
    y1 = enterNumber('Enter first y: ')
    x2 = enterNumber('Enter second x: ')
    y2 = enterNumber('Enter second y: ')

    if(subtraction):
        y2 = p - y2;

    try:
        print('\nThe sum of the points ({},{}) and ({},{}):'.format(x1,y1,x2,y2))
        point = calculator.calculateR(ecc.Point(x1,y1), ecc.Point(x2,y2))
        print('({},{})'.format(point.x, point.y))
    except ValueError as e:
        print(e)


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
        elif(choice == 2):
            n = enterNumber('Enter n: ')
            x = enterNumber('Enter x: ')
            y = enterNumber('Enter y: ')
       
            try:
                print('\nThe multiples:')
                print('\n'.join(calculator.calculateG(n, x, y)))
            except ValueError as e:
                print(e)
        elif(choice == 3):
            doAdditionOrSubtraction()
        else:
            doAdditionOrSubtraction(True)
            
        choice = printMenu()
    else:
        print('Bye!')

except ValueError as e:
    print(e)
