word = "abacd"
alpha_arr = {}
target = input("Enter the character what to cheack :")

for i in word:
    if i in alpha_arr:
        alpha_arr[i] += 1
    else:
        alpha_arr[i] = 1

if target in alpha_arr:
    print(f"{target} is present {alpha_arr[target]} times")
else:
    print(0)