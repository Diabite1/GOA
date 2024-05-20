from turtle import *

bgcolor("midnight blue")

width(6)

speed(10)

#brown house
color("firebrick")
begin_fill()
forward(150)
left(90)
forward(150)
left(90)       #base of the house
forward(150)
left(90)
forward(150)
end_fill()

penup()
goto(150,150)
pendown()

left(225)
forward(105)
left(90)      #roof
forward(105)

penup()
goto(50,0)
pendown()

color("yellow")
begin_fill()
right(135)
forward(60)
right(90)      #door
forward(50)
right(90)
forward(60)
end_fill()

penup()
goto(20,90)
pendown()

left(90)
forward(25)
left(90)
forward(25)     #window1
left(90)
forward(25)
left(90)
forward(25)

penup()
goto(130,90)
pendown()

right(90)
forward(25)
right(90)
forward(25)
right(90)         #window2
forward(25)
right(90)
forward(25)

penup()
goto(-200,-200)
pendown()

#cyan house
color("medium spring green")
begin_fill()
right(90)
forward(200)
right(90)
forward(200)
right(90)       #base of the house
forward(200)
right(90)
forward(200)
end_fill()

penup()
goto(-275,-200)
pendown()

color("purple")
begin_fill()
left(180)
forward(90)
left(90)        #door
forward(50)
left(90)
forward(90)
end_fill()

penup()
goto(-350,-75)
pendown()

right(90)
forward(35)
right(90)
forward(35)
right(90)     #window1
forward(35)
right(90)
forward(35)
right(90)
forward(35)

penup()
goto(-215,-75)
pendown()

forward(35)
right(90)
forward(35)
right(90)
forward(35)
right(90)     #window2
forward(35)
right(90)
forward(35)

penup()
goto(-200,0)
pendown()

begin_fill()
right(45)
forward(142)
left(90)
forward(142)
left(135)      #roof
forward(200)
end_fill()

penup()
goto(300,-250)
pendown()

#green house
color("green")
begin_fill()
forward(150)
left(90)
forward(150)
left(90)       #base of the house
forward(150)
left(90)
forward(150)
end_fill()

begin_fill()
left(90)
forward(50)
color("red")
left(90)
forward(60)    #door
right(90)
forward(50)
right(90)
forward(60)
end_fill()

penup()
goto(320,-125)
pendown()

forward(25)
left(90)
forward(25)
left(90)     #window1
forward(25)
left(90)
forward(25)

penup()
goto(400,-125)
pendown()

left(90)
forward(25)
left(90)
forward(25)
left(90)     #window2
forward(25)
left(90)
forward(25)

penup()
goto(300,-100)
pendown()

begin_fill()
right(135)
forward(105)
right(90)     #roof
forward(105)
end_fill()

color("yellow")
penup()
goto(530,250)
pendown()

begin_fill()
circle(radius=150)   #sun
end_fill()

penup()
goto(-500,300)
pendown()

forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)     #star
forward(20)
left(144)
forward(20)
left(144)

penup()
goto(-400,350)
pendown()

forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)

penup()
goto(-300,250)
pendown()

forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)

penup()
goto(-200,300)
pendown()

forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)

penup()
goto(-100,350)
pendown()

forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)

penup()
goto(0,250)
pendown()

forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)

penup()
goto(100,300)
pendown()

forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)

penup()
goto(200,330)
pendown()

forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)

penup()
goto(300,280)
pendown()

forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)
forward(20)
left(144)


exitonclick()
