# A program calculating an exponent modulo q
# Written by Benjamin Mestdagh

def calculate(x, a, q):
    i = 1
    while i > 0:
        result = (a**i) % q
        if result == x:
            return i
        else:
            i = i + 1


print("x = a^k mod q")

try:
    x = int(input("Enter x: "))
    a = int(input("Enter a: "))
    q = int(input("Enter q: "))
    
    print("Calculating...")

    print("k =", calculate(x, a, q))

except:
    print("Error")
