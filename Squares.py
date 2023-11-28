#Alex Flores
#November 7, 2023
#Problem 5 Squares
# The code will create a square.
import turtle
def drawSquare (t, size):
    for i in range (4):
        t.forward(size)
        t.left(90)

def main():
    wn = turtle.Screen()
    wn.bgcolor('black')
    alex = turtle.Turtle()
    alex.pensize(2)
    alex.speed(10)
    alex.color('blue')
    space = -10

    for i in range(20, 105, 20):
        drawSquare(alex,i)
        alex.up()
        alex.goto(space, space)
        alex.down()
        space = space - 10
    wn.exitonclick()
main()
