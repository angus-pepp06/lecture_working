#i = 0
#while i < 3:
 #   print("Meow")
  #  i += 1

# The above was the first attempt, it works, but it can be done in 2 more efficient ways:
#for _ in range(3):
 #   print("meow")
# & NB we use _ for a variable name, where the variable name does not matter, this is just pythonic convention.
# it will go up to but not include 3, i.e, the same as i < 3.

"another method is:"
print("Meow\n" * 3, end="")
