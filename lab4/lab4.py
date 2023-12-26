import turtle
t=turtle.Pen()
fout=open('out',"wt")

"""
W - 10px fata 
S - 10px spate
D - 45 gr dreapta
A - 45 gr stanga
F - creion sus
G - creion jos
leer/enter - stop desen
"""

l=[]
def forward():
    turtle.forward(10)
    l.append('W')

def backward():
    turtle.backward(10)
    l.append('S')

def right():
    turtle.right(45)
    l.append('D')

def left():
    turtle.left(45)
    l.append('A')

def up():
    turtle.up()
    l.append('F')

def down():
    turtle.down()
    l.append('G')
def functie():


    turtle.onkey(forward,'W')

    turtle.onkey(backward,'S')

    turtle.onkey(right,'D')

    turtle.onkey(left,'A')

    turtle.onkey(up,'F')

    turtle.onkey(down,'G')

    #turtle.onkey()



    turtle.listen()
    turtle.done()


functie()
for i in range(len(l)):
    fout.write(l[i])

fout.close()

