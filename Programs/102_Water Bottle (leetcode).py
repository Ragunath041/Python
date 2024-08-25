bottles = 15
exchange = 4
sum = 0
while bottles > 0:
    if bottles <= exchange:
        sum += bottles
        bottles = 0
    else:
        b_e = bottles % exchange
        sum += bottles - b_e
        bottles = (bottles // exchange) + (bottles % exchange)
print(sum)