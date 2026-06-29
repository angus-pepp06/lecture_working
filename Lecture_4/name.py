import sys

try:
    print("hello, my name is", sys.argv[1])
except:
    print("Please enter a name in command-line")