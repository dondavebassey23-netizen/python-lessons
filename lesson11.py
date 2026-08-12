# String manipulation
# order.strip() removes the white spaces from both ends
# order.upper() convert all letters to upper case 
# order.lower() coverts to lowercase
# order.strip().title() chain methods to strip and capitaised

# Clean the string and save the output back into a variable
# customer_name = " david "
# cleaned_name = customer_name.strip()
# proper_name = cleaned_name.capitalize()

# print("[" + proper_name + "]")

# message = "it is dry season"
# new_message = message.replace("dry", "rainy")
# # print(new_message.strip().title())
# print(new_message.strip().upper())

#STRING SLICING
# name = "Christopher"
# print(name[0:8])

# #String Formatting (Inserting Variables) f-string
# name= "John"
# drink = "Fanta"
# price = 500
# receipt = f"Order for {name}: {drink} — ₦{price:.2f}"
# print(receipt)

# customer = "Bob"
# total = 12.0
# print(f"Thank you, {customer}! Total: ₦{total:.2f}")

#System State:
raw_order_list = "latte,espresso,mocha"
menu_display = ""
# 1. Split the comma-separated string into a List
items = raw_order_list.split(",")
print(items)

# 2. Join the List using a newline character (\n) as the separator
menu_display = "\n".join(items)
print(menu_display)