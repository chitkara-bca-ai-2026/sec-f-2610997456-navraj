import math

value = float(input("enter a numerical value: "))
exponent = float(input("enter an exponent: "))
decimal_measurement = float(input("enter a decimal measurement: "))

power = math.pow(value, exponent)
square_root = math.sqrt(value)
ceil_value = math.ceil(decimal_measurement)
floor_value = math.floor(decimal_measurement)

print("\n========== mathematical results ==========")
print(f"input value         : {value}")
print(f"exponent            : {exponent}")
print("------------------------------------------")
print(f"power               : {power}")
print(f"square root         : {square_root:.4f}")
print("------------------------------------------")
print(f"decimal measurement : {decimal_measurement}")
print(f"ceiling value       : {ceil_value}")
print(f"floor value         : {floor_value}")
print("==========================================")