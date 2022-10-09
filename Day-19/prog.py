from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def turn_left():
    newheading = timmy.heading() + 10
    timmy.setheading(newheading)


def turn_right():
    newheading = timmy.heading() - 10
    timmy.setheading(newheading)


def clearthis():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(move_forward, "f")
screen.onkey(move_backward, "b")
screen.onkey(turn_left, "l")
screen.onkey(turn_right, "r")
screen.onkey(clearthis, "c")

screen.exitonclick()
