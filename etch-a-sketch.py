import turtle as t

tim = t.Turtle()
screen = t.Screen()


def move_forward():
    tim.forward(10)


def move_backward():
    tim.backward(10)


def rotate_clockwise():
    tim.right(10)


def rotate_anti_clockwise():
    tim.left(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
tim.speed("fastest")
t.onkey(key="w", fun=move_forward)
t.onkey(key="s", fun=move_backward)
t.onkey(key="d", fun=rotate_clockwise)
t.onkey(key="a", fun=rotate_anti_clockwise)
t.onkey(key="c", fun=clear_screen)
screen.exitonclick()
