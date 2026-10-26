product_name = input("enter product name: ")
price = float(input("enter price: "))
quantity = int(input("enter quantity: "))

total_price = price * quantity
amount_str = str(total_price)

print("\n********** product details **********")
print("product name :", product_name)
print("price        : rs.", price)
print("quantity     :", quantity)

print("\n********** data type details **********")
print("product_name =", type(product_name))
print("price        =", type(price))
print("quantity     =", type(quantity))
print("total_price  =", type(total_price))
print("amount_str   =", type(amount_str))

print("\n********** final bill **********")
print(f"item          : {product_name}")
print(f"unit price    : rs. {price:.2f}")
print(f"quantity      : {quantity}")
print("--------------------------------")
print(f"total amount  : rs. {total_price:.2f}")
print("********************************")

