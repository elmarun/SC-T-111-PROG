import math

x1_str = input("Input x1: ")  # do not change this line
y1_str = input("Input y1: ")  # do not change this line
x2_str = input("Input x2: ")  # do not change this line
y2_str = input("Input y2: ")  # do not change this line

dx = int(x2_str) - int(x1_str)
dy = int(y2_str) - int(y1_str)

# convert strings to ints
d = math.sqrt(dx**2 + dy**2)

print("d =", d)  # do not change this line