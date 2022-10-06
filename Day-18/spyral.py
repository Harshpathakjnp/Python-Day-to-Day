import random
import turtle
from turtle import Turtle, Screen


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


timmy_the_turtle = Turtle()
turtle.colormode(255)

screen = Screen()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("coral1")
timmy_the_turtle.speed("fastest")
for i in range(50):
    timmy_the_turtle.color(random_color())
    timmy_the_turtle.circle(100)
    current=timmy_the_turtle.heading()
    timmy_the_turtle.setheading(current+10)


screen.exitonclick()
