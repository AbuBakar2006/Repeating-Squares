import turtle

turtle.speed(30)
turtle.hideturtle()
num = 300
for i in range(1, int(num/5)):
    turtle.left(90)
    turtle.forward(num)
    turtle.left(90)
    turtle.forward(num)
    turtle.left(90)
    turtle.forward(num)
    turtle.left(90)
    turtle.forward(num)
    num -= 5

turtle.done()
