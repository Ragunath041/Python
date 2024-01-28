chain = []

for _ in range(3):  # Assuming a maximum of 10 words in the chain
    word = input()
    
    if word == "####":
        break
    
    chain.append(word)

if len(chain) == 0:
    print("No words entered.")
else:
    print("ANSWERS:\n".join(chain))
