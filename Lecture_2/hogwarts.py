# NB: !!
# Greyed out more simple, line 5, line 9&10, 
students = ["Hermione", "Harry", "Ron", "Draco"]
# This is a list, like a list of three integers from earlier meows, but, now a list of 4 strings.
# print(students[3]) - this is faded because we get to better stuff.
# This is how we can index into the list, and print only a specific value from a list of values within a variable.
# The first item in a list is at location 0, the second at 1, and so on. Lists are zero-indexed in python. 

#for student in students:
    #print (student)
    # student is a new variable, called student, not _ because we do actually use the variable. We call variables what they are unless we do not need to use it.
    # Python is supposed to be readable.
    # This nicely prints each name using a for loop.
    # No need to initialize the variable student, just introduce it and it will work.

# if instead we want to use numbers:
    # We cannot use range as that requires integers, which students a string variable is not. Therefore we use length.
    # Length gives us the length of a string. we can nest it within a range, and then it would work.

#for i in range(len(students)):
    #print(i, students[i])
    # This code now prints out the students ranked by their number, determined by position within initial string. we can use the variable i to determine what to print.

for i in range(len(students)):
    print(i+1, students[i])


# HOW DO FOR LOOPS WORK?
# 1. Creates a variable, we have called it i, it could be called anything. 
# 2. it assigns the variable, i, to the first thing in the list, and then it iterates to the second thing and so on until we reach the end of the list.
# 3. Each time i gets assigned a new variable, all of the nested code gets completed for that value of i.
# 4. In this example, as opposed to meow.pys, we are doing this to a range of a function not just a number. so :
    # for i in range(3): -- this would do something three times
    # if we had a variable n, which we asked for, and then we had "for i in range(n):" -- we would get the code done n times.
    # Because students is a list, i.e, Ron, hermione..., these are not integers they are a string format of variable, we use:
        # range(len(students)), to get the length of the variable, i.e., how many data poitns, here there are 4. and then we use the range as before.
# We added i+1, to be printed infront of the ith student, this is so it shows which position on the list the student is (irl, this could be like ranking in terms of grade)
# and it is i +1 because i is indexed to 0, and humans count from 1 not 0.

# NB adding hogwarts2.py, in which i will introduce dictionaries
