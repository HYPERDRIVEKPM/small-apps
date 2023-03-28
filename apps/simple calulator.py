def add():
    addition = True
    while addition:
        num1 = int(input('please enter a number ? '))
        num2 = int(input(f'{num1} + '))
        print(num1 + num2)
        choice = 'wrong'
        while choice not in ['Y', 'N']:
            choice = input('would you like to continue? y - n : ').upper()
        if choice == 'Y':
            addition = True
        else:
            addition = False


def sub():
    sub = True
    while sub:
        num1 = int(input('please enter a number ? '))
        num2 = int(input(f'{num1} - '))
        print(num1 - num2)
        choice = 'wrong'
        while choice not in ['Y', 'N']:
            choice = input('would you like to continue? y - n : ').upper()
        if choice == 'Y':
            sub = True
        else:
            sub = False


def multi():
    multi = True
    while multi:
        num1 = int(input('please enter a number ? '))
        num2 = int(input(f'{num1} * '))
        print(num1 * num2)
        choice = 'wrong'
        while choice not in ['Y', 'N']:
            choice = input('would you like to continue? y - n : ').upper()
        if choice == 'Y':
            multi = True
        else:
            multi = False


def div():
    div = True
    while div:
        try:
            num1 = int(input('please enter a number ? '))
            num2 = int(input(f'{num1} * '))
            print(num1 / num2)
        except ZeroDivisionError:
            print("cannot divide by zero!")
        finally:
            choice = 'wrong'
            while choice not in ['Y', 'N']:
                choice = input('would you like to continue? y - n : ').upper()
            if choice == 'Y':
                div = True
            else:
                div = False


def cal():
    cal_on = True
    while cal_on:
        choice = 9
        while choice not in [0, 1, 2, 3, 4]:
            choice = int(input('please select a option \n1 = add\n2 = sub\n3 = multi\n4 = div\nExit = 0 : '))
        if choice == 1:
            add()
        elif choice == 2:
            sub()
        elif choice == 3:
            multi()
        elif choice == 4:
            div()
        else:
            if choice == 0:
                cal_on = False
                break
            else:
                continue


cal()
