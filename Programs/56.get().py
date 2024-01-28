alpha = ["a","b","c","c","b","a"]
count = 0
for i in range(len(alpha)):
    for j in alpha:
        if alpha[i] in alpha:
            count += 1
        print(count)