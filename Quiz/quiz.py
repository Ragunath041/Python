
print("_________                            QUIZ                                _______")
name = input("Enter Your Name : ")
ch = input("Can We Start the Game, Type (Yes / No) or (1 or 0) : ")
ch = ch.lower()
score = 0
if ch == '1' or ch == "yes":
    print("Rules...")
    print("You have totally 5 questions, Which is based on simple Math problems\neach euestions carries 1 marks and the wrong question have negative marks....")
    i = 5
    while i > 0:
        if i == 5:
            q = input("What is 5 + 5 : ")
            if q == '10' or q == '10.0':
                score += 1
            else:
                score -= 1
        if i == 4:
            q = input("What is 10 - 4 : ")
            if q == '6' or q == '6.0':
                score += 1
            else:
                score -= 1
        if i == 3:
            q = input("What is the Value of PI : ")
            if q == "22/7" or q == "3.14":
                score += 1
            else:
                score -= 1
        if i == 2:
            q = input("What is the product of 8 and 10 : ")
            if q == "80" or q == "80.0":
                score += 1
            else:
                score -= 1
        if i == 1: 
            q = input("What is the value of 10 / 5 : ")
            if q == "2" or  q == "2.0":
                score += 1
            else:
                score -= 1
        i -= 1
else:
    print("you are Enter Wrong choice .........")
print("__________________________________________________________")
if ch == '1' or ch == "yes":
    match score:
        case 5:
            print(f"You got {score} marks.!")
            print("You'r performance rating : ⭐⭐⭐⭐⭐")
        case 4:
            print(f"You got {score} marks.!")
            print("You'r performance rating : ⭐⭐⭐⭐")
        case 3:
            print(f"You got {score} marks.!")
            print("You'r performance rating : ⭐⭐⭐")
        case 2:
            print(f"You got {score} marks.!")
            print("You'r performance rating : ⭐⭐")
        case 1:
            print(f"You got {score} marks.!")
            print("You'r performance rating : ⭐")
        case _:
            print(f"You got {score} marks...!")
            print("Try again....😔😔😔😔")

    print("__________________________________________________________")
