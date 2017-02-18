a = 5
b = 3

print("a : {}, b : {}".format(a, b))

print("1ere technique")

a = a + b
b = a - b
a = a - b

print("a : {}, b : {}".format(a, b))

print("2e technique")

c = a
a = b
b = c

print("a : {}, b : {}".format(a, b))

print("3e technique")

a, b = b, a

print("a : {}, b : {}".format(a, b))
