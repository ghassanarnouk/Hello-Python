print ("Hello world of Python.")
x = 6

if x == 6:
    print("x is", x)
else:
    print("x is not 1")

if x != 0:
    print("x is not 0\n")

while x >= 1:
    print("x is", x)
    x -= 1

print("")

fruits = ["apple", "banana", "orange"]

for f in fruits:
    if f != "banana":
        print("f is ", f)
    else:
        print("f is BANANA")
        break

