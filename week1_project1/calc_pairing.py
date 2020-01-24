def calculator(number_1, number_2, char):
        if char == '+':
            result = number_1 + number_2
            print(result)
        if char == '-':
            result = number_1 - number_2
            print(result)
        if char == '*':
            result = number_1 * number_2
            print(result)
        if char == '/':
            if number_2 == 0:
                print("You can not divide a number by 0")
            else:
                result = number_1 / number_2
                print(result)
   
###### main loop
while True:
    number_1 = input("Enter your first number please > ")
    number_2 = input("Enter your second number please > ")
    char = input("Enter any of these chars to calculate +,-,*,/ \nIf if you would like to quit, press 'q'")
    if char == 'q':
        break
    number_1 = int(number_1)
    number_2 = int(number_2)
    calculator(number_1, number_2, char)
