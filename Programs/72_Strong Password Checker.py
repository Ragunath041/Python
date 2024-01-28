s = input("Enter the password :")
if len(s) < 6:
    print(f"The  number of charavter is required to make a strong password {6 - len(s)}")
else:
    for i in range(len(s)):
        if s[i] != s[i+1]:
            print("Its a strong pansword")
            break
        else:
            s[i],s[i+1] = s[i+1],s[i]
            print(s)
            break
            