# coding=utf-8
# 三对正交质点做矢量合成
# 需要：
#   表盘：12 个大点（小时）和 48 个小点（分钟），以及 1 组坐标轴（浅色 RGB）
#   R #ff0000 #ffaaaa
#   G #00ff00 #aaffaa
#   B #0000ff #aaaaff
#   质点：3 对共 6 个，浅色 RGB
#   指针：3 个，实色 RGB，较大的圆点
#   效果线：
# 坐标轴分开可能更好看？六芒？
# @author       ja50n
# @time         2020-10-24-happy 2^10 day!
import turtle
import datetime
import math


# 抬起画笔，向前运动一段距离放下
def Skip(step):
    turtle.penup()
    turtle.forward(step)
    turtle.pendown()


def SetupClock(radius):
    # 建立表的外框
    turtle.reset()
    turtle.pensize(7)
    turtle.penup()
    turtle.goto(0, 0)
    for i in range(60):
        Skip(radius)
        if i % 5 == 0:
            turtle.dot(15)
        else:
            turtle.dot(6)
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()
        turtle.right(6)

    # 表盘
    turtle.color("#dddddd")
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(0)
    turtle.pendown()
    turtle.forward(radius - 20)
    turtle.backward(radius - 20 + radius - 20)
    turtle.penup()
    turtle.goto(0, 0)
    turtle.setheading(90)
    turtle.pendown()
    turtle.forward(radius - 20)
    # turtle.dot(90)
    turtle.backward(radius - 20 + radius - 20)
    turtle.update()


def getHand(name: str):
    d = {"second": 4, "minute": 5, "hour": 7, "point": 3}
    turtle.goto(d[name], 0)
    turtle.begin_poly()
    turtle.circle(d[name])
    turtle.end_poly()
    turtle.register_shape(name, turtle.get_poly())
    turtle.clear()


def Init():
    turtle.mode("logo")
    # hands
    global scnd, mnte, our, sx, sy, mx, my, hx, hy
    getHand("second")
    getHand("minute")
    getHand("hour")
    getHand("point")
    our = turtle.Turtle()
    our.shape("hour")
    our.color("#000000")
    our.fillcolor("#0000ff")
    mnte = turtle.Turtle()
    mnte.shape("minute")
    mnte.color("#000000")
    mnte.fillcolor("#00ff00")
    scnd = turtle.Turtle()
    scnd.shape("second")
    scnd.color("#000000")
    scnd.fillcolor("#ff0000")
    for hand in our, mnte, scnd:
        hand.penup()
        hand.speed(0)
        hand.goto(0, 230)
        # hand.pendown()
    hx = turtle.Turtle()
    hx.fillcolor("#aaaaff")
    hx.color("#aaaaff")
    hy = turtle.Turtle()
    hy.fillcolor("#aaaaff")
    hy.color("#aaaaff")
    mx = turtle.Turtle()
    mx.fillcolor("#aaffaa")
    mx.color("#aaffaa")
    my = turtle.Turtle()
    my.fillcolor("#aaffaa")
    my.color("#aaffaa")
    sx = turtle.Turtle()
    sx.fillcolor("#ffaaaa")
    sx.color("#ffaaaa")
    sy = turtle.Turtle()
    sy.fillcolor("#ffaaaa")
    sy.color("#ffaaaa")
    sx.pensize(6)
    sy.pensize(6)
    mx.pensize(9)
    my.pensize(9)
    hx.pensize(14)
    hy.pensize(14)
    for point in sx, sy, mx, my, hx, hy:
        point.shape("point")
        point.penup()
        point.hideturtle()

    # map
    SetupClock(250)
    turtle.hideturtle()


def Tick():
    tim = datetime.datetime.today()
    ho = tim.hour
    mi = tim.minute
    se = tim.second + tim.microsecond / 1000000
    mi += se / 60
    ho += mi / 60
    for point in hx, hy, mx, my, sx, sy:
        point.clear()
        point.goto(0, 0)
        point.pendown()
    ######
    ourr = ho * 6 / 360 * 2 * math.pi
    ourx = math.sin(ourr) * 230
    oury = math.cos(ourr) * 230
    our.goto(ourx, oury)
    hx.goto(ourx, 0)
    hy.goto(0, oury)
    mnter = mi * 6 / 360 * 2 * math.pi
    mntex = math.sin(mnter) * 230
    mntey = math.cos(mnter) * 230
    mnte.goto(mntex, mntey)
    mx.goto(mntex, 0)
    my.goto(0, mntey)
    scndr = se * 6 / 360 * 2 * math.pi
    scndx = math.sin(scndr) * 230
    scndy = math.cos(scndr) * 230
    scnd.goto(scndx, scndy)
    sx.goto(scndx, 0)
    sy.goto(0, scndy)
    # scnd.dot(10)
    # print(str(scndx) + " " + str(scndy))
    for point in sx, sy, mx, my, hx, hy:
        point.penup()
    turtle.update()
    turtle.ontimer(Tick, 100)


if __name__ == "__main__":
    turtle.tracer(False)
    Init()
    Tick()
    turtle.mainloop()
