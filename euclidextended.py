# Extended Euclidean Algorithm
# Written by Benjamin Mestdagh

class EuclidResult:
    def __init__(self, d, x, y):
        self.d = d
        self.x = x
        self.y = y


def calculate(a, b):
    x0 =  1
    xn = 1
    y0 = 0
    yn = 0
    x1 = 0
    y1 = 1
    r = a % b

    while (r > 0):
        q = a//b
        xn = x0 - q*x1
        yn = y0 - q*y1

        x0 = x1
        y0 = y1
        x1 = xn
        y1 = yn
        a = b
        b = r
        r = a % b
    
    return EuclidResult(b, xn, yn)

if __name__ == "__main__":
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    print(calculate(a,b))
