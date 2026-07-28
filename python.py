first_name = "Olatoye"
last_name = "Toyeeb"
full_name = first_name + " " + last_name 
print(full_name)

employee_age = 25
employee_info = full_name + " is " + str(employee_age) + " years old"
print(employee_info)

address = "8, Ojo street, shasha"
address += ", Oguntade, Akowonjo"
print(address)

position = "Data Analyst"
salary = 700000
experience_years = 3
employee_card = f"Employee: {full_name} | Age: {employee_age} | Position: {position}  | Salary: {salary}"
print(employee_card)

employee_code = "DEV-2026-JD-001"
department = employee_code[:3]
print(department)

employment_year = employee_code[4:8]
print(employment_year)

initials = employee_code[9:11]
print(initials)

last_three = employee_code[-3:]
print(last_three)
