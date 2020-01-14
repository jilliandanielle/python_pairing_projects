while True:

    number_1 = input("\nEnter your first number here: ")
    try:
        number_1 = int(number_1)
    except ValueError:
        number_1 = int(input("Please enter only a number: "))

    number_2 = input("\nEnter the second number here: ")
    try:
        number_2 = int(number_2)
    except ValueError:
        number_2 = int(input("Please enter only a number: "))

    operator = input("\nPick an operator [add, sub, mult, div] or type 'quit': ")

    if operator not in ['add', 'sub', 'div', 'mult']:
        break 

    if operator =='add':
        result = number_1 + number_2
        print(f"\nYour result is {result}\n")
    
    if operator =='sub':
        result = number_1 - number_2
        print(f"\nYour result is {result}\n")
    

    if operator =='mult':
        result = number_1 * number_2
        print(f"\nYour result is {result}\n")
    

    if operator =='div':
        if number_2 == 0:
            print("\nWHAT ARE YOU DOING!?\n")
            break
    result = number_1 / number_2
    print(f"\nYour result is {result}\n")
    