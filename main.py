from turtle import Turtle,Screen,colormode
from random import choice
colors = [(211, 210, 210), (189, 167, 121), (57, 90, 111), (113, 43, 35), (163, 89, 64), (210, 212, 214), (208, 211, 208), (211, 209, 210), (64, 43, 43), (171, 183, 170)]

# col()
# for i in range(len(image_color)):
#     col.append((image_color[i].rgb.r, image_color[i].rgb.g, image_color[i].rgb.b))
# print(col)
colormode(255)

paint = Turtle()
paint.shape("circle")
paint.sety(0.0)
paint.penup()
paint.setx(-170)
paint.hideturtle()
paint.speed("fastest")
y=0
while paint.ycor() < 300:
    for i in range(9):
        paint.dot(size=20)
        paint.color(choice(colors))
        paint.penup()
        paint.forward(40)
    y += 30
    paint.sety(y)
    paint.setx(-170)


screen = Screen ()
screen.exitonclick ()