employee = {
    "name": "Anita",
    "age": 29,
    "department": "Engineering"
}

employee["salary"] = 90000
employee["age"] = 30
employee["city"] = "Bengaluru"
employee["department"] = "AI Engineering"

employee1 = {
    "name": "Rahul",
    "age": 28,
    "department": "Engineering",
    "salary": 75000
}
# print(employee1)
# Use one .update() call to:

# Change age to 29
# Change salary to 85000
# Add city as "Bengaluru"
# Add experience as 5
employee1.update({
    "age": 20,
    "salary": 85000,
    "city": "Bengaluru",
    "experience": 5
})

# print(employee)
# print(employee1)

employee2 = {
    "name": "Rahul",
    "age": 29,
    "department": "Engineering",
    "salary": 85000,
    "city": "Bengaluru"
}

del employee2["city"]
removed_salary = employee2.pop("salary")
employee2.popitem() #department will be removed
print(employee2, removed_salary)
employee2.clear()
data = {
    "a": 10,
    "b": 20
}
data.clear()
print(data)

# A. "I want to remove the age key and don't care about its value." - del emplpoyee["age"]

# B. "I want to remove the salary key and use the salary value somewhere else." .pop("salary") as it will return the removed value

# C. "I want to remove the most recently added entry." .popitem() -  removes last inserted item

# D. "I want to empty the entire dictionary." - .clear()

print(employee.keys())

portfolio = {
    "name": "Gautham",
    "stocks": 25,
    "investment": 3500000
}

portfolio_copy = portfolio.copy()

portfolio_copy["stocks"] = 30

# print(portfolio)
# print(portfolio_copy)

employee3 = {
    "name": "Anita",
    "age": 30,
    "department": "AI Engineering",
    "salary": 90000
}

for key in employee3:
    print(key)

for values in employee3.values():
    print(values)
    
for key, values in employee3.items():
    print(key,': ', values)
    
# Q4 - it doesn't matter what we give either key or value by default for key in dict will return only keys by default

employee = {
    "name": "Rahul",
    "age": 32,
    "address": {
        "city": "Bengaluru",
        "state": "Karnataka",
        "pincode": 560001
    },
    "job": {
        "title": "Python Developer",
        "experience": 4
    }
}
# print(employee["name"])
# print(employee["address"]["city"])
# print(employee["job"]["title"])
# print(employee["job"]["experience"])
# employee["address"]["city"] = "Mysore"
# employee["job"]["salary"] = 1200000

# print(employee)
# employee["address"] # returns address dictionary
# # Q8 - How would you access the salary after Q6? 
# print(employee["job"]["salary"])


employees = [
    {
        "id": 101,
        "name": "Anita",
        "department": "AI Engineering",
        "salary": 1200000
    },
    {
        "id": 102,
        "name": "Rahul",
        "department": "Backend",
        "salary": 1000000
    },
    {
        "id": 103,
        "name": "Priya",
        "department": "Finance",
        "salary": 900000
    }
]

print(employees[0]["name"])
# Print Rahul's salary using list indexing + dictionary key access.
print(employees[1]["salary"])
for employee in employees:
    print(employee["name"])
for employee in employees:
    print(employee["name"], ':', employee["department"])
# Print the names of employees whose salary is greater than 950000.
for employee in employees:
    if employee["salary"] > 950000:
        print(employee["name"])
employees[-1]["salary"] = 950000
employees[0]["experience"] = 5
high_salary_employees = []
for employee in employees:
    if employee["salary"] > 950000:
        high_salary_employees.append(employee)
print(high_salary_employees)