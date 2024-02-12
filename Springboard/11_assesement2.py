a = 'Jack and Jill went to the hill'
count = 0
for i in a.split():
    if i.endswith('ill'):
        count += 1
        print(count)