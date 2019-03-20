class Square:
    square_list = []

    def __init__(self,w,l):
        self.width = w
        self.length = l
        self.square_list.append((self.width,self.length))

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.width,self.width,self.width,self.width)

sq1 = Square(1,1)
print(sq1)
sq2 = Square(2,2)
print(sq2)
sq3 = Square(3,3)
print(sq3)

print(Square.square_list)

