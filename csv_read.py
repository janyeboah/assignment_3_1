import csv

customers = open('customers.csv', 'r')

csv_file = csv.reader(customers,delimiter=',')

next(csv_file)

for row in csv_file:
    print(row)
    print(f"First Name: {row[1]}")
    print(f"Last Name: {row[2]}")
    print(f"City: {row[3]}")
    print(f"Country: {row[4]}")
    print(f"Phone: {row[5]}")
    print()
    print()
    input()