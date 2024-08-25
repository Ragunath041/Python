def inserting(arr):
    while True:
        c = int(input('(1) Inserting in Queue Concept or (2) Just Append (3) Stop: '))
        if c == 1:
            index = int(input('Enter the Index: '))
            element = int(input('Enter the Element you need to Insert: '))
            arr.insert(index, element)
        elif c == 2:
            element = int(input('Enter the Element you need to Insert: '))
            arr.append(element)
        elif c == 3:
            break
        else:
            print('Entered Wrong Input....!')

def deleting(arr):
    if len(arr) == 0:
        return False
    else:
        while True:
            print(arr)
            k = int(input('Enter the Element you want to Delete: '))
            if k in arr:
                arr.remove(k)
                print('\nDeleted...\n')
            else:
                print('\nElement not found!\n')
            i = int(input('Continue deleting? (1 for Yes, 0 for No): '))
            if i == 0:
                break
    return True

arr = []

while True:
    choice = int(input('Enter Your choice\n1 - Inserting\n2 - Deleting\n3 - Displaying\n4 - Exit\n'))
    if choice == 4:
        print(f'Your Final List is {arr}')
        break
    elif choice == 1:
        inserting(arr)
    elif choice == 2:
        if not deleting(arr):
            print('Empty!!!')
    elif 3:
        print(arr)
    else:
        print('Invalid choice!')
