import turtle

from random import*
def star1(x,y):
    turtle.penup()
    turtle.goto(x,y)
    def star(b,c,d):
        x=5
        y=0
        
        turtle.begin_fill()
        turtle.penup()
        turtle.goto(c,d)
        while x>0:
            turtle.forward(b)
            turtle.right(144)
            turtle.forward(b)
            x-=1
        turtle.end_fill()

    star(100,x,y)

    def random_color():
        randvar=randrange(0,5)
        if randvar==0:
            return ('red')
        elif randvar==1:
            return ('blue')
        elif randvar==2:
            return ('green')
        elif randvar==3:
            return ('yellow')
        else:
            return ('black')

    def length():
        randvar=randrange(5,71)

    def x():
        randvar=randrange(-280,281)

    def y():
        randvar=randrange(-200,201)

    def night_sky():
       z=int(input('How many stars do you want?'))
       a=random_color
       b=length
       c=x
       d=y
       while z>0:
           star(a,b,c,d)
           z-=1
           




def triangle(x,y):
    turtle.penup()
    turtle.begin_fill()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.goto(x,y+100)
    turtle.goto(x+100,y+100)
    turtle.goto(x,y)
    turtle.end_fill()
    turtle.penup()
    



turtle.speed(0)

def change_color_blue():
    turtle.pencolor ("blue")
    turtle.color ("blue","blue")
   
turtle.onkey(change_color_blue,"b")

def change_color_purple():
    turtle.pencolor ("purple")
    turtle.color ("purple","purple")

def change_color_green():
    turtle.pencolor ("green")
    turtle.color ("green","green")

def change_color_yellow():
    turtle.pencolor ("yellow")
    turtle.color ("yellow","yellow")
   
turtle.onkey(change_color_yellow,"y")
   
turtle.onkey(change_color_green,"g")
   
turtle.onkey(change_color_blue,"b")
turtle.onkey(change_color_purple,"p")



turtle.onscreenclick(triangle,3,True)
turtle.onscreenclick(star1,1,True)

turtle.listen()
turtle.mainloop()

