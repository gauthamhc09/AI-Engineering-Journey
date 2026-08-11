# Create a lambda that:

# Takes a number
# Returns its square


square = lambda x: x * x
cube = lambda x: x * x * x

print(square(2))
print(square(3))
print(square(4))
print(cube(2))

numbers = [1, 2, 3, 4, 5, 6]
# result
# [2, 4, 6, 8, 10, 12]
result = list(map(lambda x: x + x, numbers))
greaterThan3 = list(filter(lambda x: x > 3, numbers))
                    
print(result)
print(greaterThan3)

students = [
    ("Rahul", 82),
    ("Gautham", 95),
    ("Priya", 88),
    ("Sree", 91),
    ("Bharath", 76)
]
# 1. Sort students by marks from lowest to highest.
sorted_marks = sorted(students, key=lambda student: student[1])
# 2. Sort students by marks from highest to lowest.
sorted_marks_higher = sorted(students, key=lambda student: student[1], reverse=True)
# 3. Then create a second version where you sort students alphabetically by name.
sorted_student_names = sorted(students, key=lambda student: student[0].lower())
print(sorted_marks)
print(sorted_student_names)