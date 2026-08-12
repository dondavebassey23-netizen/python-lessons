# 1. Defining the routine (This does not run the code!)
# def brew_coffee():
#     print("Grinding espresso beans...")
#     print("Brewing hot coffee into the cup...")
#     print("Coffee is ready!")

# # 2. Calling the routine (This executes the nested lines)
# brew_coffee()

# # "customer_name" is a placeholder parameter
# def print_cup_label(customer_name):
#     print("--------------------")
#     print("Order: Hot Latte")
#     print("Name: " + customer_name)
#     print("--------------------")

# Pass real string values (arguments) into the function
# print_cup_label("Alice")
# print_cup_label("Bob")

# def print_label(current_customer):
#     print("Name on cup: " + current_customer)

# print_label("Alice")

# def order_drink(drink, size):
#     print("Dispensing " + size + " " + drink)

# order_drink("espresso", "large")

# System State:
# cups_ordered = 3
# price_per_cup = 4.50
# customer_receipt = ""

# # Definition
# def calculate_price(count, cost):
#     total = count * cost
#     return total  # Send the calculated float back

# # Call and save the returned value in a variable
# customer_receipt = calculate_price(cups_ordered, price_per_cup)

# print(customer_receipt)

# System State (New):
cups_ordered = 3
price_per_cup = 4.50
customer_receipt = 13.50 #(Changed from "")

# def add_tax(subtotal):
#     return subtotal * 1.08

# final_total = add_tax(10.0)
# print(final_total)

def make_custom_drink(base_drink, milk_type, sugar_packets):
    # Assemble the descriptive string step-by-step
    description = f"{base_drink} with {milk_type} milk"
    
    if sugar_packets > 0:
        description = description + f" and {sugar_packets} sugar packets"
        
    return description

# Generate distinct order strings
order1 = make_custom_drink("Latte", "almond", 2)
order2 = make_custom_drink("Cappuccino", "whole", 0)

print(order1) # "Latte with almond milk and 2 sugar packets"
print(order2) # "Cappuccino with whole milk"