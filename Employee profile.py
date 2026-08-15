
first_name = 'Toyeeb'
last_name = 'Olatoye'

full_name = first_name + ' ' + last_name

address = '8 ojo street'
address += ', shasha akowonjo Lagos'

# Employee Demographic and Narrative Construction
employee_age = 28
employee_info = full_name + ' is ' + str(employee_age) + ' years old'
print(employee_info)

# Professional Experience Mapping
experience_years = 5
experience_info = 'Experience: ' + str(experience_years) + ' years'
print(experience_info)

# Position and Compensation Formatting
position = 'Data Analyst'
salary = 75000
employee_card = f'Employee: {full_name} | Age: {employee_age} | Position: {position} | Salary: ${salary}'
print(employee_card)


employee_code = 'DEV-2026-JD-001'

# Extracting Department Token (DEV)
department = employee_code[0:3]
print(department)

# Extracting Registration Year Token (2026)
year_code = employee_code[4:8]
print(year_code)

# Extracting Employee Initials Token (JD)
initials = employee_code[9:11]
print(initials)
