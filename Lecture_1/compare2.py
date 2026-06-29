x = int(input("What is x?"))
y = int(input("What is y?"))

# goal here is to find out if x = y, its actually doing slightly less than compare.py was, but its simple

if x > y or x < y:
    print("x does not equal y")
else: 
    print("x equals y")

# alternatively use: if x != y:, return, print("x does not equal y")
