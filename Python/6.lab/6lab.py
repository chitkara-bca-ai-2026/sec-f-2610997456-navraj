
customer_name = input("enter customer name: ")
garment_name = input("enter garment name: ")
price = float(input("enter price of one garment: "))
quantity = int(input("enter number of garments: "))

total_amount = price * quantity

print("\n----------- clothing store -----------")
print("              customer bill")
print("--------------------------------------")
print(f"customer name : {customer_name}")
print(f"garment name  : {garment_name}")
print(f"price per unit: rs. {price:.2f}")
print(f"quantity      : {quantity}")
print("--------------------------------------")
print(f"total amount  : rs. {total_amount:.2f}")
print("--------------------------------------")
print("        thank you for shopping!")
print("--------------------------------------")