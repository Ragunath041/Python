#lex_auth_01269363490743091290

def display(num):
    message=""
    #write your logic here
    if num % 3 == 0 and num % 5 == 0:
     message = 'Zoom'
    elif num % 5 == 0:
     message = 'Zap'
    elif num % 3 == 0:
     message = 'Zip'
    else:
     message = 'Invaid'
    return message

#Provide different values for num and test your program
message=display(45)
print(message)
