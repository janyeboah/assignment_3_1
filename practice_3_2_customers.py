import csv

# Open empty object called customers to host the customers csv file
customers = open('customers.csv', 'r')

# Use csv.reader to read in the customers.csv
# delimiter=',' means that each row of data is separted by commas ','
reader = csv.reader(customers, delimiter=',')

# Create or open an empty file called customer_country.csv
outfile = open('customer_country.csv', 'w', newline='')


# Loop through each row of the customers.csv file
# Using 'enumerate' initializes a counter that tracks or counts
#   each row in the customers.csv file
for i, row in enumerate(reader):

    # i=0 is the first row of the intended new file, customer_country.csv
    # Use the first row as the column names of the data
    if i == 0:
        output_row = 'FullName,Country\n'
    else:

        # combine the 2nd column (FirstName or column index 1) and 
        # the 3rd column (LastName or column index 2)
        # to create the full name
        full_name = row[1] + ' ' + row[2]

        # Extract the country or column index 4
        country = row[4]

        # Combine the full name and country into a single string
        output_row = f"{full_name},{country}\n"
    
    # write the newly created row to the customer_country.csv file
    outfile.write(output_row)


outfile.close()
print(f"The total number of customers read is {i}")