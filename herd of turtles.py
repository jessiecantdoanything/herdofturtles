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
eliza.color("black")
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

eliza.up()
eliza.goto(-67, -40)
eliza.setheading(-60)
eliza.width(5)
eliza.down()
eliza.circle(80, 120)

eliza.fillcolor("black")

for i in range(-35, 105, 70):
   eliza.up()
   eliza.goto(i, 35)
   eliza.setheading(0)
   eliza.down()
   eliza.begin_fill()


eliza.hideturtle()


turtle.exitonclick()
