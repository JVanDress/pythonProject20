              #DICTIONARY  keys are immunitble only  VALUES ARE ASSOCIATED WITH A KEY
              #dict(x=1, y=2) =====  KEYWORD ARGUMENT
              # map a key to a value


point = dict(x=1, y=2)
point["x"] = 10
point["z"] = 20
if "a" in point:
    print(point["a"])
    print(point.get("a", 0))
del point["x"]
print(point)
for key, value in point.items():
    print(key, value)
    














