import os 

def add():
    os.system('cls')
    print('Addition')

    more = 'y'
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    current_sum = num1 + num2
    values = 2
    print(f'Current Sum: {current_sum}')

    while more.lower() == 'y':
        more = (input('More numbers? y/n:'))
        
        while more.lower() not in ['y','n']:
            more = input('Invalid input. More numbers? y/n: ')
        if more.lower() == 'n':
            break
        num = float(input('Enter number: '))
        current_sum += num
        values += 1
        print(f'Current Sum: {current_sum}')
    return [current_sum, values]
        
def sub():
    os.system('cls')
    print('Subtraction')

    more = 'y'
    num1 = float(input('Enter first number: ')) 
    num2 = float(input('Enter second number: '))
    current_ans = num1 - num2
    values = 2
    print(f'Current Answer: {current_ans}')

    while more.lower() == 'y':
        more = input('More numbers? y/n: ')

        while more.lower() not in ['y','n']:
            more = input('Invalid input. More numbers? y/n: ')
        if more.lower() == 'n':
            break
        num = float(input('Enter number: '))
        current_ans -= num
        values += 1
        print(f'Current Answer: {current_ans}')
    return [current_ans, values]

def multiply():
    os.system('cls')
    print('Multiplication')

    more = 'y'
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    current_product = num1 * num2
    values = 2
    print(f'Current Product: {current_product}')

    while more.lower() == 'y':
        more = input('More numbers? y/n: ')

        while more.lower() not in ['y','n']:
            more = input('Invalid input. More numbers? y/n: ')
        if more.lower() == 'n':
            break
        num = float(input('Enter number: '))
        current_product *= num
        values += 1
        print(f'Current Product: {current_product}')
    return [current_product, values]

def divide():
    os.system('cls')
    print('Division')

    more = 'y'
    num1 = float(input('Enter first number: '))
    num2 = float(input('Enter second number: '))
    current_quotient = num1 / num2
    values = 2
    print(f'Current Quotient: {current_quotient}')

    while more.lower() == 'y':
        more = input('More numbers? y/n: ')

        while more.lower() not in ['y','n']:
            more = input('Invalid input. More numbers? y/n: ')
        if more.lower() == 'n':
            break
        num = float(input('Enter number: '))
        current_quotient /= num
        values += 1
        print(f'Current Quotient: {current_quotient}')
    return [current_quotient, values]


def cal():
    quit = False
    while not quit:
        print('Simple Calculator')
        print('Enter a for addition')
        print('Enter s for subtraction')
        print('Enter m for multiplication')
        print('Enter d for division')
        print('Enter q to quit')

        choice = input("Selected operation: ")

        if choice == 'a':
            result = add()
            print(f'Ans = ', result[0], 'total values = ', result[1])
        elif choice == 's':
            result = sub()
            print(f'Ans = ', result[0], 'total values = ', result[1])
        elif choice == 'm':
            result = multiply()
            print(f'Ans = ', result[0], 'total values = ', result[1])
        elif choice == 'd':
            result = divide()
            print(f'Ans = ', result[0], 'total values = ', result[1])
        elif choice == 'q':
            break

if __name__ == '__main__':
    cal()

    



