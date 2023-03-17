import csv

# Save a CSV file of your transactions in the same folder as this project and put the name below
FILE = ''

def finance_manager(file):
    sum = 0 
    transactions = []
    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        header = next(csv_reader)
        for row in csv_reader:
            #get name, amount, currency
            name = row[4]
            amount = float(row[7])
            date = row[1]
 
            transaction = (date, name, amount)
            sum += amount
            transactions.append(transaction)
    print(f"The sum of your transactions this month is {sum}")
    print('')
    return transactions

print(finance_manager(FILE))