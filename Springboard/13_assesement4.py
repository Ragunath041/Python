a , b = 10 , 40
def function(a):
    global b
    a , b = 20 , 50
    print(a,end=" ")
    print(b,end=" ")

function(30)
print(a,end=" ")
print(b,end=" ")
