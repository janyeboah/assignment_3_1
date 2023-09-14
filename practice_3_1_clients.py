clients = open('clients.txt', 'r')


for i, row in enumerate(clients):
    if i < 5:
        print(row.rstrip('\n'))