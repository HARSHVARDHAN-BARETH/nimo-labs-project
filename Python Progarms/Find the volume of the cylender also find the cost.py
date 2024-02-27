import math

costPerLtr = 40
radius = float(input("radius of the cylender : "))
height = float(input("height of the cylender : "))

volume = math.pi * radius*2*height
totalCost = volume * costPerLtr

print(f"Volume of the Cylender is : {volume : .2f}")
print(f"totalCost of the Cylender is : {totalCost : .2f}")

# o/p:
#     radius of the cylender : 5
#     height of the cylender : 6
#     volume of the cylender is 471.24 cubic units
#     totalCost is Rs. 18849.56