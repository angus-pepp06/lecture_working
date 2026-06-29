#n = int(input("What is n?"))
#for _ in range(n):
 #   print("#")

#def main():
 #   print_column(3)
#def print_column(height):
 #   for _ in range(height):
  #      print("#")
#main()
def main():
    print_square(3)

def print_square(size):
    # For each row in square:
    for i in range(size):
        # For each brick in row:
        for j in range(size):
            # Print brick
            print("#", end="")
        print()

main()