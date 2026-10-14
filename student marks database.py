#student marks database
students={
    "Rahul":89,
    "ravi":92,
    "anil":78,
    "keerthi":94
    }
highest=max(students,key=students.get)
print("Topper=",highest)
print("Marks=",students[highest])
