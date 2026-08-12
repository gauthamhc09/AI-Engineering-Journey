SCHOOL_NAME = "AI Engineering Academy"

print("=" * 40)
print(" " * 5, "STUDENT PERFORMANCE SYSTEM", " " * 5)
print("=" * 40)

def calculate_total(marks):
    if not marks:
        return 0
    
    return marks[0] + calculate_total(marks[1:])

def calculate_average(total_marks, number_of_subjects=3):
    return total_marks/number_of_subjects

def calculate_grade(average):
    grade = ""
    if average >= 90:
        grade = "A+"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    return grade

def student_ranking(python_marks, math_marks, science_marks):
    marks = [("Python", python_marks), ("Math", math_marks), ("Science", science_marks)]
    sorted_marks = sorted(marks, key=lambda mark: mark[1], reverse=True)
    print("-" * 50)
    n=0
    for mark in sorted_marks:
        print(f"{n + 1}. {mark[0]}: {mark[1]}") 
        n+=1
    print("-" * 50)
    
def generate_report(student_name, roll_number, math_marks, 
                    science_marks, python_marks, total_marks, 
                    average_marks, grade):
    print("=" * 40)
    print(" " * 5, "STUDENT REPORT", " " * 5)
    print("=" * 40) 
    print("\n")
    print("School", " " * 9, ": ", SCHOOL_NAME)
    print("Student", " " * 8, ": ", student_name)
    print("Roll Number", " " * 5, ": ", roll_number)
    print("\n")
    print("Math", " " * 9, ": ", math_marks)
    print("Science", " " * 9, ": ", science_marks)
    print("Python", " " * 9, ": ", python_marks)
    print("\n")
    print("Total", " " * 9, ": ", total_marks)
    print("Average", " " * 9, ": ", average_marks)
    print("Grade", " " * 9, ": ", grade)
    print("\n")
    print("STUDENT Ranking")
    student_ranking(python_marks, math_marks, science_marks)

def student_input():
    student_name = input("Enter Student Name: ")
    roll_number = int(input("Enter Roll Number: "))
    
    math_marks = int(input("Enter Math Marks: "))
    science_marks = int(input("Enter Science Marks: "))
    python_marks = int(input("Enter Python Marks: "))
    
    return [student_name, roll_number, math_marks, science_marks, python_marks]

def main():
    name, roll, math, science, python = student_input()
    marks = [math, science, python]
    total_marks = calculate_total(marks)
    average_marks = calculate_average(total_marks)
    grade = calculate_grade(average_marks)
        
    generate_report(name, roll, math, science, python, total_marks, average_marks, grade)
        
main()