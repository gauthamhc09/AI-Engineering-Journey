print("=" * 50)
print("WELCOME TO STUDENT INFORMATION SYSTEM")
print("=" * 50)

#Get student information
name = input("What is your name? ")
age = int(input("What is your age? "))
course = input("Which course you are enrolled for? ")
marks_scored = int(input("Enter marks scored: "))

total_marks = 600
percentage = (marks_scored * 100) / total_marks

result = "passed" if percentage >=30 else "failed"
print(f"Your result is {percentage:.2f}. So you have {result}")

