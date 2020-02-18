class Rectangle:
    def __init__(self, length,breadth, unit_cost):
        self.length = length
        self.breadth = breadth
        self.unit_cost = unit_cost
    def get_area(self):
        return self.length * self.breadth
    def calculate_cost(self):
        area= self.get_area()
        return area*self.unit_cost
r = Rectangle(length=int(input('Enter a length')),breadth= int(input('Enter a breadth')),unit_cost=int(input('Enter unit cost')))

#r = Rectangle(10,20,2000)
print("Area of Rectangle: %s sq units"  %(str(r.get_area())))
print("Cost of rectangular field: Rs%s" %(str(r.calculate_cost())))