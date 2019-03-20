class Shape:
    def what_am_i(self):
        print("I am a shape")

class Rectangle(Shape):
    def __init__(self,w,l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return self.width + self.length

    def print_size(self):
        print(self.calculate_perimeter())

class Square(Shape):
    def __init__(self,w,l):
        self.width = w
        self.length = l

    def calculate_perimeter(self):
        return self.width + self.length

    def print_size(self):
        print(self.calculate_perimeter())
        
    def change_size(self,w,l):
        self.width += w
        self.length += l

rectangle = Rectangle(1,2)
rectangle.what_am_i()

square = Square(3,3)
square.what_am_i()

rectangle.print_size()
square.print_size()

square.change_size(1,1)
square.print_size()
