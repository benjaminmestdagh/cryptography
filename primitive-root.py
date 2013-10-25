# Program to check if a is a primitive root mod q
# Written by Benjamin Mestdagh

def calculate(a, q):
    powers = []

    for i in range(1, q):
        result = (a**i) % q
        if result in powers:
            return False
        else:
            powers.append(result)

    return True

try:
    a = int(input("Enter a: "))
    q = int(input("Enter q: "))
    result = calculate(a,q)

    if result:
        print('{0} is a primitive root mod {1}'.format(a, q))
    else:
        print('{0} is NOT a primitive root mod {1}'.format(a,q))

except:
    print("Error")
