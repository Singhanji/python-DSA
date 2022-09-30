# How Class works

# creating a class

class ComplexNumber:
    real = 0                    # properties of the class- real and imaginary
    imaginary = 0

# creating a constructor

    def __init__(self, r, i):   # creating a constructor or a special method(function) inside the class that allows us to define the properties while creating also it is called/invoked automatically when the object of the class is created.
        self.real = r
        self.imaginary = i

# creating a function output so that I do not have to write print statement again-2 in below functions 

    def output(self):           # The first argument of a method of a class if generally referred as "self". Self refers to the calling object.
        print(f"{self.real} + {self.imaginary}i")

# creating an OBJECT(x) of the class(ComplexNumber)

x = ComplexNumber(5, 3)
x.output()                      # Here 'Calling Object' is --> x

# creating another OBJECT(y) of the class(ComplexNumber)

y = ComplexNumber(12, -2)
y.output()                     # Here 'Calling Object' is --> y



