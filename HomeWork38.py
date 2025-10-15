class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        if isinstance(other, Fraction):
            return Fraction(other.a * self.a, other.b * self.b)
        raise ValueError('Can multiple only with another Fraction')

    def __add__(self, other):
        if isinstance(other, Fraction):
            new_a = self.a * other.b + other.a * self.b
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        raise ValueError('Can stack only with another Fraction')

    def __sub__(self, other):
        if isinstance(other, Fraction):
            new_a = self.a * other.b - other.a * self.b
            new_b = self.b * other.b
            return Fraction(new_a, new_b)
        raise ValueError('Can sub only with another Fraction')

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b == other.a * self.b
        return False

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b > other.a * self.b
        raise ValueError('Can compare with another Fraction')

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.a * other.b < other.a * self.b
        raise ValueError('Can compare with another Fraction')

    def __str__(self):
        return f"Fraction: {self.a}, {self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')
