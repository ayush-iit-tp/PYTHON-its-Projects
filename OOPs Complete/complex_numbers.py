# Creating our own class for getting complex numbers
#from numbers import Complex

class Complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imG = imaginary

    def showNumber(self):
        print("The Complex number is:",self.real,"i+", self.imG,"j")

    def __add__(self, num_2):
        newReal = self.real + num_2.real
        newImag = self.imG + num_2.imG
        return Complex(newReal, newImag)

    def __sub__(self, num_2):
        newReal = self.real - num_2.real
        newImag = self.imG - num_2.imG
        return Complex(newReal, newImag)
'''
Dunder Functions: which are like these: __add__ and __sub__ methods and have double underscore in starting and ending. 
'''
num1 =Complex(real=5.0, imaginary=-4.0)
num1.showNumber()

num2 = Complex(real=4.0, imaginary=6.0)
num2.showNumber()

num3 = num1.__add__(num2)
num3.showNumber()

num4 = num1.__sub__(num2)
num4.showNumber()