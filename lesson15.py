#1. What is a Higher-Order Function?
#A Higher-Order Function is simply:
#A function that can accept another function as an argument or return a function.
def greet(name):
    return f"Hello {name}"

def execute(func):
    return func("David")

print(execute(greet))

#2. Lambda Functions
#Lambda lets us write the same thing in one line:
#lambda parameter: expression
square = lambda x: x * x
print(square(4))

# map()
# The lesson describes map() as applying a tool to every item in a collection.

menu_prices = [4.50, 3.50, 5.00]
updated = list(map(lambda x: x + 0.50, menu_prices))

print(updated) # Output: [5.0, 4.0, 5.5]

drinks = ["latte", "espresso", "mocha"]
loud_drinks = list(map(lambda d: d.upper(), drinks))
print(loud_drinks)

# METHOD 1
prices = [100, 200, 300]

new_prices = list(
    map(lambda p: p + 50, prices)
)

# Or METHOD 2
print(new_prices)

prices = [100, 200, 300]

result = map(lambda x: x + 50, prices)

print(list(result))

# Maping Dictionaries

products = [
    {"name": "Laptop", "price": 500},
    {"name": "Phone", "price": 300},
    {"name": "Tablet", "price": 400}
]

new_products = list(
    map(
        lambda product: {
            "name": product["name"],
            "price": product["price"]
        },
        products
    )
)

print(new_products)


# filter() : Filter cIt checks every item and asks: if it should pass , if the anser is true
#it keeps it , if t is false , it discards it

#Menu State:
menu_items = [
      {"name": "Espresso", "price": 3.50},
      {"name": "Latte", "price": 4.50},
      {"name": "Mocha", "price": 5.00}
    ]
filtered_menu = []
# Strain out any item with a price greater than 4.50
filtered_menu = list(filter(lambda item: item["price"] <= 4.50, menu_items))
print(filtered_menu)

prices = [100, 500, 200, 800]

cheap = list(
    filter(lambda p: p < 400, prices)
)

print(cheap) # print(list(cheap)) can also be used

# 5. sorted(): Sorting means arranging items.

numbers = [11, 3, 8, 5, 27]
print(sorted(numbers))

# sorting dictionaries 
products = [
    {"name": "Laptop", "price": 500},
    {"name": "Phone", "price": 300},
    {"name": "Tablet", "price": 400}
]
# sorting by price
sorted_products = sorted(
    products,
    key=lambda item: item["price"] # the key is introduces because Python doesn't automatically know how to compare dictionaries
)

print(sorted_products)

# How This Connects to AI Agents
# Imagine your AI agent receives:
tickets = [
    {"user": "A", "priority": 5},
    {"user": "B", "priority": 1},
    {"user": "C", "priority": 3}
]

urgent = list(
    filter(lambda f:f["priority"] >= 3, tickets)
)
print(urgent)

sorted_tickets = sorted(
    urgent,
    key=lambda t: t["priority"],
    reverse=True
)
print(sorted_tickets)

# Assignment

prices = [10, 20, 30, 40]

# List Comprehension equivalent:
doubled_prices = [x * 2 for x in prices]

print(doubled_prices)  # Output: [20, 40, 60, 80]