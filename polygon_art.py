import turtle
import random

turtle.speed(0)
turtle.bgcolor('black')
turtle.tracer(0)
turtle.colormode(255)

def get_new_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    get_new_color = (r, g, b)
    return get_new_color

class Polygon():
    def __init__(self, num_sides, size, orientation, location, color, border_size):
        self.num_sides = num_sides
        self.size = size
        self.orientation = orientation
        self.location = location
        self.color = color
        self.border_size = border_size

    def draw(self):
        turtle.penup()
        turtle.goto(self.location[0], self.location[1])
        turtle.setheading(self.orientation)
        turtle.color(self.color)
        turtle.pensize(self.border_size)
        turtle.pendown()
        for _ in range(self.num_sides):
            turtle.forward(self.size)
            turtle.left(360/self.num_sides)
        turtle.penup()

    def move(self):
        turtle.penup()
        self.location = [random.randint(-300, 300), random.randint(-200, 200)]
        turtle.goto(self.location[0], self.location[1])

class PolygonArt():
    def __init__(self):
        turtle.speed(0)
        turtle.bgcolor('black')
        turtle.tracer(0)
        turtle.colormode(255)

    def run():
        i = 30
        num = int(input('Which art do you want to generate? Enter a number between 1 to 9 inclusive: '))
        while i > 0:
            size = random.randint(50, 150)
            orientation = random.randint(0, 90)
            location = [random.randint(-300, 300), random.randint(-200, 200)]
            color = get_new_color()
            border_size = random.randint(1, 10)
            reduction_ratio = 0.618
            num_level = 2

            if num == 1:
                num_sides = 3
                polygon_art = Polygon(num_sides, size, orientation, location, color, border_size)
                polygon_art.draw()
            elif num == 2:
                num_sides = 4
                polygon_art = Polygon(num_sides, size, orientation, location, color, border_size)
                polygon_art.draw()
            elif num == 3:
                num_sides = 5
                polygon_art = Polygon(num_sides, size, orientation, location, color, border_size)
                polygon_art.draw()
            elif num == 4:
                num_sides = random.randint(3, 5)
                polygon_art = Polygon(num_sides, size, orientation, location, color, border_size)
                polygon_art.draw()
            elif num == 5:
                num_sides = 3
                polygon_art = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_level, reduction_ratio)
                polygon_art.draw()
            elif num == 6:
                num_sides = 4
                polygon_art = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_level, reduction_ratio)
                polygon_art.draw()
            elif num == 7:
                num_sides = 5
                polygon_art = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_level, reduction_ratio)
                polygon_art.draw()
            elif num == 8:
                num_sides = random.randint(3, 5)
                polygon_art = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_level, reduction_ratio)
                polygon_art.draw()
            elif num == 9:
                num_sides = random.randint(3, 5)
                num_level = random.randint(1, 2)
                polygon_art = EmbeddedPolygon(num_sides, size, orientation, location, color, border_size, num_level, reduction_ratio)
                polygon_art.draw()
            i -= 1


        turtle.done()
        
class EmbeddedPolygon(Polygon):
    def __init__(self, num_sides, size, orientation, location, color, border_size, num_level, reduction_ratio):
        super().__init__(num_sides, size, orientation, location, color, border_size)
        self.num_level = num_level
        self.reduction_ratio = reduction_ratio

    def draw(self): # overriding draw()  in Polygon
        if self.num_level == 1:
            super().draw()
        else:
            while self.num_level > 0:
                super().draw()
                self.size *= self.reduction_ratio
                self.location[0] += self.size * (1 - self.reduction_ratio) / 2
                self.location[1] += self.size * (1 - self.reduction_ratio) / 2
                super().draw()
                self.num_level -= 1


x=PolygonArt
x.run()
