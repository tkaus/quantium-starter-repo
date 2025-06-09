import csv
print("working")

data = []

with open ('data/daily_sales_data_0.csv', mode='r') as file:
    reader = csv.reader(file, delimiter=',')
    line_count = 0 
    for row in reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            if row[0] == 'pink morsel':
                print('working')

                price = row[1]
                price = price.replace("$", "")
                price = float(price)
                quantity = float(row[2])
                sales = price*quantity

                item_from_list = {
                    "price":row[1],
                    "sales":sales,
                    "region":row[4]
                }
                data.append(item_from_list)


                # print(sales)
                # print(row[3])
                # print(row[4])

            line_count += 1

with open ('output_data.csv', mode = "w") as output_file:
    writer = csv.writer(output_file, delimiter=',', quotechar='""', quoting=csv.QUOTE_MINIMAL)
