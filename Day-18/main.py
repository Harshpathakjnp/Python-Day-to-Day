from turtle import Turtle,Screen

timmy_the_turtle = Turtle()

screen = Screen()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("coral3")
noofsides =50
angle = 360//noofsides
for i in range(noofsides):
    timmy_the_turtle.forward(5)
    timmy_the_turtle.left(angle)


screen.exitonclick()



