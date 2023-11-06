#1:

import turtle
t=turtle.Pen()
t2=turtle.Pen()
t3=turtle.Pen()

def dreptunghi():
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(100)

    t.up()

    t.right(90)
    t.forward(70)
    t.right(90)
    t.forward(30)
    t.down()
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(25)


#2:

def curba():
    for i in range(200):
        t.right(1)
        t.forward(1)

def curba2():
    for i in range(200):
        t2.left(1)
        t2.forward(1)


def inima():
    t.left(140)
    t.forward(110)
    curba()

    t2.left(400)
    t2.forward(110)
    curba2()



#3:

def case():
    t.forward(200)
    t2.up()
    t2.right(180)
    t2.forward(50)
    t2.right(90)
    t2.down()
    t2.forward(-200)
    t2.right(270)
    t2.forward(80)
    t2.right(90)
    t2.forward(200)
    t2.right(90)
    t2.forward(80)

    t.right(90)
    t.forward(100)
    t.right(90)
    t.forward(200)
    t.right(90)
    t.forward(100)
    t.up()
    t.right(90)
    t.forward(70)
    t.right(90)
    t.forward(30)
    t.down()

    t2.up()
    t2.right(90)
    t2.forward(70)
    t2.right(90)
    t2.forward(30)
    t2.down()

    t2.right(90)
    t2.forward(50)
    t2.right(90)
    t2.forward(25)
    t2.right(90)
    t2.forward(50)
    t2.right(90)
    t2.forward(25)
    t2.up()


    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(25)
    t.right(90)
    t.forward(50)
    t.right(90)
    t.forward(25)

    t2.up()
    t2.left(90)
    t2.forward(130)
    t2.down()
    t2.left(180)
    t2.forward(100)
    t2.left(90)
    t2.forward(20)
    t2.left(90)
    t2.forward(100)


    t.up()
    t.forward(70)
    t.left(180)
    t.down()
    t.forward(60)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(60)

    t3.left(45)
    t3.forward(141)
    t3.right(90)
    t3.forward(141)

    t3.right(45)
    t3.right(90)
    t3.up()
    t3.forward(250)
    t3.down()
    t3.right(45)
    t3.forward(56.5)
    t3.left(90)
    t3.forward(56.5)

def main():
    a=input("Ce desenam? 1? 2? 3? ")

    if(a=='1'):
        dreptunghi()
    else:
        if(a=='2'):
            inima()
        else:
            if(a=='3'):
                case()



main()