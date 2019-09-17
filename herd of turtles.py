import turtle

scn = turtle.Screen()
jr = turtle.Turtle()
chris = turtle.Turtle()
gary = turtle.Turtle()
eliza = turtle.Turtle()
gary.begin_fill()



gary.shape("turtle")
gary.color("Gold")
chris.shape("square")
chris.color("Black")
chris.speed(5)
chris.turtlesize(.5)
jr.shape("triangle")
jr.color("Rosy Brown")
jr.speed(5)
eliza.shape("circle")
eliza.color("Light Pink")
eliza.speed(5)

gary.penup()
gary.goto(0, -200)
gary.pendown()
gary.circle(200)
gary.end_fill()

chris.penup()
chris.left(40)
chris.forward(35)
chris.left(5)
chris.forward(5)
chris.pendown()
chris.forward(40)
chris.right(45)
chris.shape("circle")
chris.pendown()
chris.shapesize(3,2,1)
chris.fillcolor("black")

jr.penup()
jr.goto(-47, 53)
jr.pendown()
jr.shape("circle")
jr.shapesize(3,2,1)
jr.fillcolor("black")

eliza.penup()
eliza.right(90)
eliza.forward(90)
eliza.right(-90)
eliza.forward(90)
eliza.right(90)
eliza.pendown()
# for i in range(360):
#     eliza.forward(.75)
#     eliza.right(.5)
# eliza.right(90)
eliza.("arc")





turtle.exitonclick()