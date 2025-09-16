# Graficaci-n-Sistemas
Repositorio De Trabajos Para La Materia de Graficación

import turtle

screen = turtle.Screen()
screen.bgcolor("White")
t = turtle.Turtle()
t.speed(3)
t.pensize(2)

EN ESTA BLOQUE DE AQUI IMPORTE A LA TORTUGA PARA PODER HACER LOS DIBUJOS Y PUSE UN FONDO DE COLOR BLANCO EN LA LINEA DE "screen.bgcolor("White")" t en la linea de "t.speed(3)" declare la velocidad de la tortuga y en la linea de "t.pensize(2)" simplemente declare la velocidad de la misma

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

EN ESTE BLOQUE DE AQUI DEFINI LA FUNCION DE CIRCULO CON SU COORDENADAS x, y CON SU RADIO Y COLOR DE RELLENO Y DE AHI EL LAPIZ SE LEVANTA CON " t.penup()" Y CON "t.goto(x, y - radio)" ES A DONDE EL LAPIZ VA A CAER PARA DIBUJAR EN ESAS COORDENADAS Y YA CON t.color AGREGAMOS UN COLOR PARA LA FIGURA Y DE AHI VAMOS CON UN IF EN DONDE SI SE DECLARA UN RELLENO CON UN COLOR, LA FIGURA SE LLENARA DE ESTE MISMO Y DE AHI SE VE EL RADIO DEL CIRCULO

def linea(x_principio, y_principio, x_final, y_final, color):
    t.penup()
    t.goto(x_principio, y_principio)
    t.pendown()
    t.color(color)
    t.goto(x_final, y_final)

EN ESTE BLOQUE DE AQUI ES CASI LO MISMO QUE EL CIRCULO YA QUE LEVANTAMOS EL LAPIZ Y SOLO ELEGIMOS LAS COORDENADAS Y EL COLOR DE LA LINEA Y YA CON EL "t.goto(x_final, y_final)" SOLO DIREMOS EN DONDE TERMINARA DE DIBUJAR LA LINEA

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

EN ESTE BLOQUE QUE ES EL TRIANGULO, TAMBIEN VOLVEMOS A LO MISMO DEL LAPIZ Y EL RELLENO SOLO CON LA DIFERENCIA DE QUE AQUI DECLARAMOS UN FOR EN DONDE HACEMOS UN BUCLE PARA LOS 3 LADOS DEL TRIANGULO Y CON EL " t.forward(tamaño)" HACEMOS QUE SE HAGA UNA LINEA DE 100 PIXELES Y CON EL "t.left(120)" HACEMOS QUE GIRE 120 GRADOS PARA LA IZQUIERDA HACIENDO UN TRIANGULO EQUILATERO DE TRES LADOS IGUALITOS

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

EN ESTE BLOQUE HACEMOS EL CUADRADO CON LAS MISMAS LINEAS DE LAPIZ Y DE RELLENO PERO CON LA DIFERENCIA DE QUE AHORA TENEMOS UN BUCLE DE 4 LADOS CON ESTA LINEA DE CODIGO "for _ in range(4):" Y DE AHI DECLARAMOS EL TAMAÑO DE NUESTRO CUADRADO Y REPETIMOS LO MISMO QUE EL TRANGULO CON ESTA LINEA "t.right(90)" PARA HACER LOS CUATRO LADOS IGUALES DE NUESTRO CUADRADO