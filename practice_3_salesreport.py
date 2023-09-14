import csv

sales = open('salesreport.csv', 'r')

reader = csv.reader(sales, delimiter=',')

outfile = open('salesreportFINAL.csv', 'w', newline='')

for i, row in enumerate(reader):
    if i == 0:
        output_row = 'Customer ID,Total\n'
    else:
        output_row = f"{row[0]},{row[1]}\n"
    
    # write the newly created row to the customer_country.csv file
    outfile.write(output_row)