#print("hello, world)
# So this is an unterminated string literal. Because it is a string data type, and it needs to be terminateed with quotation marks.
# syntax errors need to be fixed by yourself, they are often typos.

# Many other errors are run-time errors

# Number.py - imagine this is in here:
#x = int(input("What is x?"))
# print(f"x is {x}")
# this will work, but we need to be paying attention, code defensively to reduce the chance of the it failing.
#while True:
   # try:
   #     x = int(input("What is x?"))
    # this code will try to do line 13. if something goes wrong, line 16 will happen.
    #except ValueError:
   ##     print("x is not an integer")
    # if nothing has gone wrong on line 13, line 19 will be done.
   #### else:
     ###   break
#####print(f"x is {x}")
# THE ABOVE WAS GREAT, BUT ADDING COMPLEXITY


#def main():
  #  x = get_int()
 #   print(f"x is {x}")
#def get_int():
    #while True:
    #    try:
   #         return int(input("What is x?"))
  #      except ValueError:
 #           print("x is not an integer")

#main()


def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            return int(input("What is x?"))
        except ValueError:
            pass

main()
# this version is less aggressive than the one before, it simply re-prompts the user for x 
