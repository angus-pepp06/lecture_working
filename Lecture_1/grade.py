# NB lines 2-14 are my original attempt which worked perfectly, but not efficiently. Therefore lines 19-32 have the current code.
# Score = int(input("Score: "))
#if 70 <= Score <=100:
 #   print("Grade is a First")
#elif 60 <= Score <=69:
 #   print("Grade is a 2:1")
#elif 50 <= Score <=59:
 #   print("Grade is a 2:2")
#elif 40 <=Score <=49:
 #   print("Grade is a Pass")
#elif 0> Score or Score > 100:
 #   print("Score is impossible, must be between 0 and 100.")
#else:
 #   print("Grade is a fail :(")


# We can also, because we are using elif, not if, actually simplifiy further, new code incoming and i will grey the rest out:

Score = int(input("Score: "))
if 70 <= Score :
    print("Grade is a First")
elif 60 <= Score:
    print("Grade is a 2:1")
elif 50 <= Score :
    print("Grade is a 2:2")
elif 40 <=Score :
    print("Grade is a Pass")
elif 0> Score or Score > 100:
    print("Score is impossible, must be between 0 and 100.")
#this is obviouly a slight improvement, and it works because we only ask the second Q if the score is less than 70, therefore we implicitly know the upper bound already.
else:
    print("Grade is a fail :(")
# Alternatively, to not include the impossible score thing, simply this at line 10:
# else:
    #print("Grade is a fail :(")