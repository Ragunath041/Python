import turtle
window = turtle.Screen()
man = turtle.Turtle()
man.speed(1)
colors = ["red","green","yellow"]
for c in colors:
    for i in range(36):
        for j in range(36):
            man.color(j)
            man.forward(10)
            man.right(10)
        man.right(10)
turtle.exitonclick()