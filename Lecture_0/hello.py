# First, ask the user for their name - note input seems to say, this is the input, and the response is the named variable.
name = input ("What is your name? ").strip().title()
# Then say hello to them. - These hash comments are really useful with large coding.
print(f"Hello, {name}")
# Now if I only want to address someone by their first name:
first, last = name.split(" ")
print (f"Hello, {first}")