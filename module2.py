def printArea():
    width = input("What's the width of the house? ")
    height = input("What's the height of the house? ")
    area = int(width) * int(height)
    print(f"The square footage of the house is {area}")
    
printArea()

def printCirc():
    diameter = input("What's the diameter of the circle? ")
    circumference = 3.14 * int(diameter)
    print(f"The circumference of the circle is {circumference}")

printCirc()