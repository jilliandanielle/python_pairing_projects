while True:

    n1 = input("\nEnter your first number here: ")
    try:
        n1 = int(n1)
    except ValueError:
        n1 = int(input("Please enter only a number: "))

    n2 = input("\nEnter the second number here: ")
    try:
        n2 = int(n2)
    except ValueError:
        n2 = int(input("Please enter only a number: "))

    operator = input("\nPick an operator [add, sub, mult, div] or type 'quit': ")

    if operator not in ['add', 'sub', 'div', 'mult']:
        break 

    if operator =='add':
        result = n1 + n2
        print(f"\nYour result is {result}")
    
    if operator =='sub':
        result = n1 - n2
        print(f"\nYour result is {result}")
    

    if operator =='mult':
        result = n1 * n2
        print(f"\nYour result is {result}")
    

    if operator =='div':
        if n2 == 0:
            print("\nWHAT ARE YOU DOING!?\n")
            break
        result = n1 / n2
        print(f"\nYour result is {result}\n")
    