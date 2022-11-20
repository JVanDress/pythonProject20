numbers = [1, 2, 3, 4, 4, 4, 4, 4]  #unpack into multiple var
first, *other, last = numbers
#if you are not using the *var and packing into a new
#var then
#when you use * python will get all the numbers or whatever
# and pack them into a new list that you must name with a
#new var
print(first, last)
print(other)






