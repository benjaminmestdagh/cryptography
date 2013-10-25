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
    print(powers)    
    return True

try:
    a = int(input("Enter a: "))
    q = int(input("Enter q: "))

    print(calculate(a, q))
except:
    print("Error")
