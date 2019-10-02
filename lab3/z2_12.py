from graph import *


brushColor(171, 223, 136)
polygon([[0,0],[500,0],[500,600],[0,600]])
brushColor(42,209,209)
polygon([[0,0],[0,250],[100,240],[150,260],[250,250],[255,275],[250,300],[260,325],[250,350],[340,360],[350,340],[400,350],[500,350],[500,600],[500,0]])
brushColor(180, 180, 181)
polygon([[0,0],[0,250],[100,240],[150,260],[250,250],[255,275],[250,300],[260,325],[250,350],[340,360],[350,340],[400,350],[500,350],[400,200],[360,175],[330,200],[270,150],[200,220],[130,175],[60,75]])
brushColor(114, 201, 52)
penColor(114, 201, 52)
c=canvas()
def clumba(X1,Y1,s):
    circle((3*X1 - 10*s) / 3, (Y1*3 + 80*s) / 3, 75*s)
    def flower(x1,y1,x2,y2):
        c.create_oval(x1, y1, x2, y2, fill="yellow")
        c.create_oval(x1 + 40*s, y1+5*s, x2 + 20*s, y2, fill="white")
        c.create_oval(x1 + 30*s, y1 + 15*s, x2 + 10*s, y2 + 10*s, fill="white")
        c.create_oval(x1 + 20*s, y1+20*s, x2, y2+15*s, fill="white")
        c.create_oval(x1 + 10*s, y1+20*s, x2-10*s, y2+15*s, fill="white")
        c.create_oval(x1, y1+15*s, x2-20*s, y2+10*s, fill="white")
        c.create_oval(x1-10*s,y1+5*s,x2-30*s,y2,fill="white")
        c.create_oval(x1, y1-10*s, x2 - 20*s, y2-15*s, fill="white")
        c.create_oval(x1+10*s, y1-15*s, x2-10*s, y2-20*s, fill="white")
        c.create_oval(x1+20*s, y1-15*s, x2, y2-20*s, fill="white")
        c.create_oval(x1+30*s, y1-10*s, x2 +10*s, y2 -15*s, fill="white")
        c.create_oval(x1+35*s, y1-5*s, x2 + 15*s, y2 -10*s, fill="white")
    flower(X1-25*s,Y1-7.5*s,X1+25*s,Y1+7.5*s)
    flower(X1+5*s,Y1+38*s,X1+55*s,Y1+62*s)
    flower(X1-65*s,Y1+18*s,X1-15*s,Y1+42*s)


clumba(400,480,0.5)
clumba(490,440,0.5)
clumba(470,360,0.4)
clumba(400,390,0.3)
clumba(490,580,0.4)
clumba(30,300,0.3)


# s-относительный параметр рамера,o-отвечает за зеркальное отражение
def lama(x, y, s, o):
    def legs(x, y):
        c.create_oval(x, y, x + 15*s*o, y + 10*s, fill="white")
        c.create_oval(x, y, x + 10*s*o, y - 30*s, fill="white")
        c.create_oval(x, y - 21*s, x + 10*s*o, y - 52*s, fill="white")
    legs(x,y)
    legs(x-32*s*o,y)
    legs(x-55*s*o,y-15*s)
    legs(x-17*s*o,y-15*s)
    c.create_oval(x + 10*s*o, y - 67*s, x + 25*s*o, y - 120*s, fill="white")
    c.create_oval(x-65*s*o,y-50*s,x+25*s*o,y-82*s,fill="white")
    c.create_oval(x+12*s*o,y-112*s,x+37*s*o,y-130*s,fill="white")
    c.create_oval(x+20*s*o,y-117*s,x+37*s*o,y-125*s,fill="pink")
    c.create_oval(x+27*s*o,y-120*s,x+37*s*o,y-125*s,fill="black")
    c.create_oval(x+22*s*o,y-122*s,x+37*s*o,y-125*s,fill="white")
    brushColor("white")
    penColor("Black")
    polygon([[x+15*s*o,y-117*s],[x+7*s*o,y-125*s],[x+15*s*o,y-122*s]])
    polygon([[x+16*s*o,y-120*s],[x+8*s*o,y-127*s],[x+17*s*o,y-125*s]])

lama(110,310,0.5,1)
lama(170,270,0.5,1)
lama(190,340,0.5,-1)
lama(480,480,1.5,-1)
lama(0,780,2.5,1)

run()





