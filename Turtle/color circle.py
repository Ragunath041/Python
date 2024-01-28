import turtle
window = turtle.Screen()
man = turtle.Turtle()
def color():
    for i in range(36):
        man.forward(10)
        man.turn(10)
colors = ["red","yellow","blue","green","purple","orange"]
for i in colors:
    man.color(i)
    man.circle()
    man.turn(60)