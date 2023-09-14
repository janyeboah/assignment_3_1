import csv

employeePay = open('EmployeePay.csv', 'r')

reader = csv.reader(employeePay, delimiter=',')
next(reader)


for row in reader:

    input("Press Enter to print the info of next employee: ")

    total_salary = float(row[3])*(float(row[4]) + 1) 

    print(f"ID: {row[0]}")
    print(f"EmpFName: {row[1]}")
    print(f"EmpLName: {row[2]}")
    print(f"Salary: {row[3]}")
    print(f"Bonus: {row[4]}")

    print(f"Total salary: {total_salary}")
    
    
