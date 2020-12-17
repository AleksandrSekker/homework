from math import pi, pow

def rectangle(a,b):
    return a * b

def triangle(h,a):
    return 0.5 * h * a

def circle(r):
    return pi * pow(r,2)

chouse_figure = input('Choose figure: ')
if chouse_figure == 'rectangle':
    print(rectangle(int(input('Chouse number: ')), int(input('Chouse second number: ')))),
elif chouse_figure == 'triangle':
    print(triangle(int(input('Chouse number: ')), int(input('Chouse second number: ')))),
elif chouse_figure == 'circle':
    print(circle(int(input('Chouse number: '))))