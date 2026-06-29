# In this file i am using dictionaries for the first time, to associate students to a house. 
# #We could use a simple list format, and agree that the first student in students is linked with the first item in linked lists, 
# But this gets very messy when we have multiple linked characteristics e.g., age, gender, house, grades. 
# The dictionary function is much cleaner
#students = {
   # "Hermione": "Gryffindor",
    #"Harry": "Gryffindor", 
    #"Ron": "Gryffindor",
    #"Draco": "Slytherin",
#}}
#print(students["Hermione"])
#print(students["Harry"])
#print(students["Ron"])
#print(students["Draco"])

# NB whereas lists only allow for us to use numbers for identification, here, using a dictionary, we can use words to index python.

#for student in students:
    #`print(student, students[student], sep=", ")



# NB, NOW DOING WITH A DATABASE, WHERE WE HAVE MULTIPLE CHARACTERISTICS; THIS REQUIRES THAT WE USE A LIST OF DICTIONARIES, AS FOLLOWS:
students = [
    {"name":"Hermione", "house":"Gryffindor", "patronus":"Otter"},
    {"name":"Harry", "house":"Gryffindor", "patronus":"Stag"},
    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack Russell Terrier"}, 
    {"name":"Draco", "house":"Slytherin", "patronus":None},
]
for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")