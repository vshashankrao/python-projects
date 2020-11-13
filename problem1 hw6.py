'''
Shashank Rao
RUID: 185005733
'''
from poly import Polynomial

class Quadratic(Polynomial):
    def __init__(self, quad = 0, linear = 0, const = 0):
            Polynomial.__init__(self, (quad, 2), (linear, 1), (const, 0))
            self._a = quad
            self._b = linear
            self._c = const
            
    def addterm(self, coeff, exp):
        if ((exp > 2) or (exp <= -1)):
            raise Exception('The exponent is not part of the quadratic exponent bounds')   
        else:
            Polynomial.addterm(self, coeff, exp)

        
    def __add__(self, other):
        value = super().__add__(other)
        coeffs = value._coeffs
        return Quadratic(coeffs[2], coeffs[1], coeffs[0])

    def __sub__(self,other):
        value = super().__sub__(other)
        coeffs = value._coeffs
        return Quadratic(coeffs[2], coeffs[1], coeffs[0])

    def __mul__(self,other):
        value = super().__mul__(other)
        if (value.degree() == 2):
            coeffs = added._coeffs
            return Quadratic(coeffs[0], coeffs[1], coeffs[0])
        else:
            return value

    def scale(self, s):
        scaled = Polynomial.scale(self, s)
        coeffs = scaled._coeffs
        return Quadratic(coeffs[2], coeffs[1], coeffs[0])

    def roots(self):
        roots = []
        a = self._a
        b = self._b
        c = self._c
        if (a != 0):
            if (b * b > 4 * a * c):
                d = ((b ** 2 - 4 * a * c) ** .5)
                num1 = -b + d
                num2 = -b - d
                a1 = num1 / (2 * a)
                a2 = num2 / (2 * a)
                roots.append(a1)
                roots.append(a2)
            elif (b * b == 4 * a * c):
                roots.append((-1 * b) / (2 * a))
        elif (b != 0):
            roots.append((-1 * c) / b)
        elif (c != 0):
            pass
        else:
            roots = [0 for x in range(3)]
        return roots
