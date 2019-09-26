from graph import *


brushColor(68,232,76)
polygon([[0,0],[500,0],[500,600],[0,600]])
brushColor(42,209,209)
polygon([[0,0],[0,250],[100,240],[150,260],[250,250],[255,275],[250,300],[260,325],[250,350],[340,360],[350,340],[400,350],[500,350],[500,600],[500,0]])
brushColor("gray")
polygon([[0,0],[0,250],[100,240],[150,260],[250,250],[255,275],[250,300],[260,325],[250,350],[340,360],[350,340],[400,350],[500,350],[400,200],[360,175],[330,200],[270,150],[200,220],[130,175],[60,75]])
brushColor(18,163,59)
circle(400,500,75)
c=canvas()

def flower(x1,y1,x2,y2):
    c.create_oval(x1, y1, x2, y2, fill="yellow")
    c.create_oval(x1 + 40, y1+5, x2 + 20, y2, fill="white")
    c.create_oval(x1 + 30, y1 + 15, x2 + 10, y2 + 10, fill="white")
    c.create_oval(x1 + 20, y1+20, x2, y2+15, fill="white")
    c.create_oval(x1 + 10, y1+20, x2-10, y2+15, fill="white")
    c.create_oval(x1, y1+15, x2-20, y2+10, fill="white")
    c.create_oval(x1-10,y1+5,x2-30,y2,fill="white")
    c.create_oval(x1, y1-10, x2 - 20, y2-15, fill="white")
    c.create_oval(x1+10, y1-15, x2-10, y2-20, fill="white")
    c.create_oval(x1+20, y1-15, x2, y2-20, fill="white")
    c.create_oval(x1+30, y1-10, x2 +10, y2 -15, fill="white")
    c.create_oval(x1+35, y1-5, x2 + 15, y2 -10, fill="white")



flower(410,510,460,535)
flower(330,490,380,515)
flower(380,440,430,465)


def legs(x,y):
    c.create_oval(x, y, x + 30, y + 20, fill="white")
    c.create_oval(x, y, x + 20, y - 60, fill="white")
    c.create_oval(x, y - 45, x + 20, y - 105, fill="white")
def lama(x, y):
    legs(x,y)
    legs(x-75,y)
    legs(x-110,y-30)
    legs(x-35,y-30)
    c.create_oval(x + 20, y - 135, x + 50, y - 240, fill="white")
    c.create_oval(x-130,y-100,x+50,y-165,fill="white")
    c.create_oval(x+25,y-225,x+75,y-260,fill="white")
    c.create_oval(x+40,y-235,x+65,y-255,fill="pink")
    c.create_oval(x+55,y-240,x+65,y-250,fill="black")
    c.create_oval(x+45,y-245,x+60,y-250,fill="white")
    brushColor("white")
    polygon([[x+30,y-235],[x+15,y-250],[x+30,y-245]])
    polygon([[x+32,y-240],[x+17,y-255],[x+35,y-250]])



lama(200,500)

run()



run()






