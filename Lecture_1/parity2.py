def main():
    x =int(input("What is x?"))
    if is_even(x):
        print("x is even")
    else: 
        print("x is odd")

#def is_even(n):
 #   if n%2 == 0:
  #      return True
   # else:
    #    return False
    # Better definition of is_even:

def is_even(n):
    return n%2 == 0
    # the expression is asking if the remainder of n/2 is 0. if it is, n must be even, if it isnt n must be odd. but the n%2==2, only returns true or false,
    # ie., n%2 == 0, returns a Boolean form anyway.
main()

