import math

def area_of_circle(radius):
    area = math.pi*radius*radius  # Formula for area of a circle: A = π * r^2
    return area

radius = float(input("Enter the radius of the circle: "))
area = area_of_circle(radius)
print(f"The area of the circle with radius {radius} is: {area}")