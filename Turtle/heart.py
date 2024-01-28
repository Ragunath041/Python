import turtle as t
t.bgcolor("white")
t.title("Heart Shape")
def draw_heart():
    t.fillcolor("red")
    t.begin_fill()
    t.left(140)
    t.forward(200)
    for _ in range(200):
        t.right(1)
        t.forward(2)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(2)
    t.forward(200)
    t.end_fill()
draw_heart()
t.hideturtle()
t.exitonclick()
