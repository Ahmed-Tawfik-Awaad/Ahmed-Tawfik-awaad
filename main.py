import math


class Shape:

    def calc_area(self):
        pass

    def calc_permater(self):
        pass


class Circle(Shape):

    def __init__(self, raduis):
        self.raduis = int(raduis)

    def calc_area(self):
        return math.pi*self.raduis**2

    def calc_permater(self):
        return (2*math.pi)*self.raduis


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area(self):
        return self.width*self.length

    def calc_permater(self):
        return 2*(self.length+self.width)


class Traingle(Shape):
    def __init__(self, base, hieght, side1, side2, side3):
        self.base = base
        self.hieght = hieght
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def calc_area(self):
        return 0.5 * self.base, self.hieght

    def calc_permater(self):
        return self.side1 + self.side2 + self.side3


while True:

    print("press 1 to calc circle area")
    print("press 2 to calc circle perimeter")
    print("press 3 to calc rectangle area")
    print("press 4 to calc rectangle perimeter")
    print("press 5 to calc triangle area")
    print("press 6 to calc triangle perimeter")
    print("press 7 to exit")
    print("================================================")

    user_input = int(input("inter your choice = "))
    if user_input == 1:
        r = int(input("inter the raduis: "))
        dayra = Circle(r)
        cir_area = dayra.calc_area()
        print("circle area = ", cir_area)
        print("============================================")

    if user_input == 2:
        qtter = int(input("inter The raduis = "))
        dayr = Circle(qtter)
        cir_per = dayr.calc_permater()
        print("Circle Permater = ", dayr)
        print("=============================================")

    if user_input == 3:
        Length = int(input("inter ractangle length : "))
        Width = int(input("inter rectangle width : "))
        morbeh = Rectangle(Length, Width)
        rec_area = morbeh.calc_area()
        print("rectangle area = ", rec_area)
        print("================================================")
    if user_input == 4:
        Length = int(input("inter ractangle length : "))
        Width = int(input("inter rectangle width : "))
        morbeh = Rectangle(Length, Width)
        rec_area = morbeh.calc_permater()
        print("rectangle area = ", rec_area)
        print("================================================")
    if user_input == 5:
        basee = int(input("enter the base = "))
        heighte = int(input("enter The hieght = "))
        side1e = int(input("enter side 1 =  "))
        side2e = int(input("enter side 2 = "))
        side3e = int(input("enter side 3 = "))
        area = Traingle(basee, heighte, side1e, side2e, side3e)
        rec_tria = area.calc_area()
        print("triangle area = ", rec_tria)
        print("=========================================")
    if user_input == 6:
        basee = int(input("enter the base = "))
        heighte = int(input("enter The hieght = "))
        side1e = int(input("enter side 1 =  "))
        side2e = int(input("enter side 2 = "))
        side3e = int(input("enter side 3 = "))
        area = Traingle(basee, heighte, side1e, side2e, side3e)
        rec_tria = area.calc_permater()
        print("triangle area = ", rec_tria)
        print("========================================")
    if user_input == 7:
        print("thanks ! ")
        exit()
