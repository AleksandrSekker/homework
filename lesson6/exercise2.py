from math import pi
def calculate_square(choose):
    """calculation square rectangle, triangle, circle"""
    
    def rectangle(width, height):
        return(width * height)
    def triangle(base, vertical_height):
        return((base * vertical_height) / 2)
    def circle(radius):
        return(pi * radius**2)
    if choose == 'rectangle':
        print(rectangle(23, 15))
    elif choose == 'triangle':
        print(triangle(10, 15))
    elif choose == 'circle':
        print(circle(10))
calculate_square(str(input('Choose square which you calculate: ')))