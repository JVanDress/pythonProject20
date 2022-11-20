#Imagine this as a shopping list.  this is a tuple

items = [
    ("Product1", 10),
    ("Product2", 9),           # Items with open bracket and close below is a block of values with prices in the
    ("Product3", 12),
]


items.sort(key=lambda item:item[1])
print(items)

