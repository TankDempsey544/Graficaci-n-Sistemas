import turtle

screen = turtle.Screen()
screen.bgcolor("White")
t = turtle.Turtle()
t.speed(3)
t.pensize(2)

def circulo(x, y, radio, relleno):
    t.penup()
    t.goto(x, y - radio)
    t.pendown()
    t.color(relleno)

    if relleno:
        t.begin_fill()
        t.fillcolor(relleno)

    t.circle(radio)

    if relleno:
        t.end_fill()

def linea(x_principio, y_principio, x_final, y_final, color):
    t.penup()
    t.goto(x_principio, y_principio)
    t.pendown()
    t.color(color)
    t.goto(x_final, y_final)

def triangulo(x, y, tamaño, relleno):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(relleno)

    if relleno:
        t.begin_fill()
        t.fillcolor(relleno)

    for _ in range(3):
        t.forward(tamaño)
        t.left(120)

    if relleno:
        t.end_fill()

def cuadrado(x, y, relleno, tamaño):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(relleno)

    if relleno:
        t.begin_fill()
        t.fillcolor(relleno)

    for _ in range(4):
        t.forward(tamaño)
        t.right(90)

    if relleno:
        t.end_fill()

cuadrado(-100, 100, "blue", 100)
triangulo(0, 100, 100, "yellow")
circulo(100, 0, 50, "green")
linea(0, -10, 0, -50, "purple")

turtle.done()
