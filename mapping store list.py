#Imagine this as a shopping list.  this is a tuple

items = [
    ("Product1", 10),
    ("Product2", 9),           # Items with open bracket and close below is a block of values with prices in the
    ("Product3", 12),
]

# the following is a great clean way to use the map function to get the prices

x = map(lambda item: item[1], items)
for item in x:
    print(item)




