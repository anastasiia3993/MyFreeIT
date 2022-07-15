#Task 6.1

def write(*args):
    print('Type the name of file:')
    mode = 'w'
    file = open(str(input()), mode)
    print('Type your string:')
    string = str(input())
    file.write(string)

write()


#Task 6.2

def season(*args):
    print('Type a number of mounth:')
    a = int(input())
    if 1 <= a <= 2 or a == 12:
        print('winter')
    elif 3 <= a <= 5:
        print('spring')
    elif 6 <= a <= 8:
        print('summer')
    elif 9 <= a <= 11:
        print('autumn')
    else:
        print('You should write a number from 1 to 12!')

season()


#Task 6.3

def square(*args):
    print('Type a side of square:')
    b = float(input())
    p = b * 4
    S = b * b
    d = b * (2 ** 0.5)
    result = (p, S, d)
    print(result)

square()

#Task 6.4

def bank(*args):
    print('Type amont of money:')
    a = float(input())
    print('Type amount of years:')
    years = int(input())
    c = 1
    S = 0
    while c <= years:
        a = a + (a * 0.1)
        c += 1
    print(a)

bank()

#Task 6.5

from time import time


def timer_func(func):
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func


@timer_func
def count(n):
    print("There is my decorated function:")
    for i in range(n):
        i += 1
        print(i)


count(10)
