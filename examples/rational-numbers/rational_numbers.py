from __future__ import division

import fractions

class Rational(object):
    def __init__(self, numer, denom):
        rational_gcd = fractions.gcd(numer,denom)
        self.numer = numer/rational_gcd
        self.denom = denom/rational_gcd

    def __eq__(self, other):
        if type(self) == type(other):
            return self.numer == other.numer and self.denom == other.denom
        else:
            return round((self.numer/self.denom),8) == round(other,8)

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return (self.numer/self.denom) + (other.numer/other.denom)

    def __sub__(self, other):
        return (self.numer/self.denom) - (other.numer/other.denom)

    def __mul__(self, other):
        return (self.numer/self.denom) * (other.numer/other.denom)

    def __truediv__(self, other):
        return (self.numer*other.denom) / (self.denom*other.numer)

    def __abs__(self):
        self.numer = abs(self.numer)
        self.denom = abs(self.denom)
        return self

    def __pow__(self, power):
        return Rational(self.numer ** power, self.denom ** power)

    def __rpow__(self, base):
        return base ** (self.numer/self.denom)



