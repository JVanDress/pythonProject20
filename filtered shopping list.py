#Imagine this as a shopping list.  this is a tuple that is blocked
items = [
    ("Product1", 10),
    ("Product2", 9),           # Items with open bracket and close below is a block of values with prices in the
    ("Product3", 12),
]


prices = [item[1] for item in items]

filtered = [item for item in items if item[1] >= 10]

print(filtered)





