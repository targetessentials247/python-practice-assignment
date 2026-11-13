# 1. Take customer's name as input
customer_name = input("Enter customer's name: ")

# 2. Take names and prices of 3 products as input
product1_name = input("Enter name of Product 1: ")
product1_price = float(input(f"Enter price of {product1_name}: "))

product2_name = input("Enter name of Product 2: ")
product2_price = float(input(f"Enter price of {product2_name}: "))

product3_name = input("Enter name of Product 3: ")
product3_price = float(input(f"Enter price of {product3_name}: "))

# 3. Calculate Subtotal
subtotal = product1_price + product2_price + product3_price

# 4. Determine the discount
if subtotal >= 5000:
    discount_rate = 0.20  # 20% discount
elif subtotal >= 3000:
    discount_rate = 0.10  # 10% discount
elif subtotal >= 1000:
    discount_rate = 0.05  # 5% discount
else:
    discount_rate = 0.0   # No discount

# Calculate discount amount and final total
discount = subtotal * discount_rate
final_total = subtotal - discount

# 5. Display the shopping summary using formatted strings (f-strings)
print(f"Customer Name: {customer_name}\n")
print(f"Product 1: {product1_name}")
print(f"Price: {product1_price}\n")
print(f"Product 2: {product2_name}")
print(f"Price: {product2_price}\n")
print(f"Product 3: {product3_name}")
print(f"Price: {product3_price}\n")
print(f"Subtotal: {subtotal}")
print(f"Discount: {discount}")
print(f"Final Total: {final_total}")