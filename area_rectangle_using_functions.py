def area_of_rectangle(length, width):
    
    area = length * width  # Formula for area of a rectangle: A = length * width
    return area

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = area_of_rectangle(length, width)
print(f"The area of the rectangle with length {length} and width {width} is: {area}")