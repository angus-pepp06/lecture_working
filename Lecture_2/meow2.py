 # The goal of meow2.py is to incorporate asking the user how many times the cat should meow.
while True:
    n = int(input("How many times should the cat meow?"))
    if n > 0:
        break
for _ in range(n):
    print("Meow")
