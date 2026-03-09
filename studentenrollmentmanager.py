#Program Title : Student Enrollment Manager *: Create a Python code to demonstrate the use of sets and perform set operations (union, intersection, difference) to manage student enrollments in multiple courses / appearing for multiple entrance exams like CET, JEE, NEET etc.
#Name : Gaurav
#Roll No. : 19
#Branch : Electronics Engineering
#DOP : 19/02/2026       DOS : 26/02/2026

jee = {"Gaurav", "Shreya", "Ayush", "Rihan"}
cet = {"Pratosh", "Parimeeta", "Shreya", "Gaurav"}
neet = {"Shreya", "Prathamesh", "Rihan", "Parimeeta"}

print("Students in JEE:", jee)
print("Students in CET:", cet)
print("Students in NEET:", neet)
all_students = jee.union(cet, neet)
print("\nStudents appearing in at least one exam:", all_students)
jee_cet = jee.intersection(cet)
print("\nStudents appearing in both JEE and CET:", jee_cet)
jee_only = jee.difference(cet)
print("\nStudents appearing in JEE but not CET:", jee_only)
cet_neet = cet.intersection(neet)
print("\nStudents appearing in both CET and NEET:", cet_neet)