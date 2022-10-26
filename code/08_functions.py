# 2022-10-17, Em Heisig (hheisig51)
# This assignment takes 6 inputs (of 3 coordinate pairs)
# and returns the area of their triangle, or returns an error

def isfloat(num):
    if len(num) < 6: # Checking if 6 items have been inputted
        return f"ERR: Insufficient inputs"
    else:
        try: # if there are 6 inputs, this checks if they also all are floats. If they are, the coordinate pairs are printed
            float(num[0])
            float(num[1])
            float(num[2])
            float(num[3])
            float(num[4])
            float(num[5])
            return f"Input #1: ({coords[0]}, {coords[1]})\nInput #2: ({coords[2]}, {coords[3]})\nInput #3: ({coords[4]}, {coords[5]})"
        except ValueError: # if one of the inputs is not a float, a ValueError happens
            return f"ERR: One of the inputs is not a number"

def area(triangle): # calculates the area of the triangle from the 3 coordinate pairs
    x_1 = float(coords[0]) 
    y_1 = float(coords[1])
    x_2 = float(coords[2])
    y_2 = float(coords[3])
    x_3 = float(coords[4])
    y_3 = float(coords[5])
    triangle = abs(((x_1*y_2)+(x_2*y_3)+(x_3*y_1)-(y_1*x_2)-(y_2*x_3)-(y_3*x_1))/2) # formula to calculate the area
    if triangle <= 0: # the area cannot be 0 or less than 0
        return f"ERR: Coordinates do not make a triangle"
    if triangle > 0:
        return f"The area is: {triangle}"

while True:
    print(f"\nFormat: x1,y1,x2,y2,x3,y3\nPlease enter ALL of your coordinates:")
    coords = input().split(',', 6) # splits the input into 6 pieces, separated via comma
    print(f"\n{isfloat(coords)}\n") # either prints an error or the coordinate pairs
    print(f"{area(coords)}") # prints the valid area, or an error
