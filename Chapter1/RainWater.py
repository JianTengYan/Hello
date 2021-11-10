import math

# Calculate rainfall in gallons for some number of inches on 1 arce
inches_str = input ("How many inches of fain have fallen: ")
inches_int = int(inches_str)
volume = (inches_int/12)*43560
gallons = volume*7.48051945
print (inches_int, "in. rain on 1 arce is ", gallons, "gallons")

# Calculate rainfall in gallons for some number of inches on 1 arce
inches_float = float(inches_str)
print (inches_float, "in. rain on 1 arce is ", gallons, "gallons")
