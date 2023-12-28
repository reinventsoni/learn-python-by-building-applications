from random import randint


class Point:
    """
    This is the point class representing a point (X,Y) in the 2-dimension
    coordinate system
    """

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        print(f"X coordinate: {self.x} and Y coordinate: {self.y}")

    def falls_in_rectangle(self, my_rectangle):
        if my_rectangle.point1.x < self.x < my_rectangle.point2.x \
                and my_rectangle.point1.y < self.y < my_rectangle.point2.y:
            return True
        else:
            return False


class Rectangle:
    """
    This is a rectangle class representing a rectangle in the 2-dimension
    space and characterised by storing the coordinates of diagonally
    opposite points
    """

    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

    def area(self):
        length = self.point2.x - self.point1.x
        height = self.point2.y - self.point2.y
        return length * height


# Create rectangle object
rectangle = Rectangle(Point(randint(0, 9), randint(0, 9)),
                      Point(randint(10, 19), randint(10, 19)))

# Print rectangle coordinates
print("Rectangle Coordinates: ",
      rectangle.point1.x, ",",
      rectangle.point1.y, "and",
      rectangle.point2.x, ",",
      rectangle.point2.y)

# Get point and area from user
user_point = Point(float(input("Guess x: ")), float(input("Guess y: ")))
user_area = float(input("Guess rectangle area: "))

# Print out the game result
print("Your point was inside rectangle: ", user_point.falls_in_rectangle(rectangle))
print("Your area was off by: ", rectangle.area() - user_area)
