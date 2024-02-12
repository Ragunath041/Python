lst = [10 , 20 , 0 , 40 , 0]
def test():
    try:
        a = 3
        if lst[a] / lst[a + 1] > 0:
            value = a + 1
    except ZeroDivisionError:
        print("1")
    except IndexError:
        print("2")
    finally:
        print("4")
    print("5")
test()