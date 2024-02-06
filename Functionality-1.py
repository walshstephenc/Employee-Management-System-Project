# Get input from user
employeeName = input("Enter employee name:")
employeeSSN = input("Enter employee SSN:")
employeePhone = input("Enter employee phone number:")
employeeEmail = input("Enter employee email:")
employeeSalary = input("Enter employee salary:")

# Print employee information
print("-" * 28 + " " + employeeName + " " + "-" * 28)
print("SSN:", employeeSSN)
print("Phone:", employeePhone)
print("Email:", employeeEmail)
print("Salary:", "$" + employeeSalary)
