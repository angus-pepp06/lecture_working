# This is no better than mario.py, it is just a different way of doing it, i.e, without as many variables - it is personal preference.

def main():
    print_square(3)

def print_square(size):
    # For each row in square:
    for i in range(size):
       print_row(size)

def print_row(width):
    print("#" * width)
main()

# Actually no that is better.
#A lthough my preference, is this:
def main():
    print_square(3)
def print_square(size):
    for i in range(size):
         print("#" * size)
main()