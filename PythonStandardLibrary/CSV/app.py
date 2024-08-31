import csv
# -------------------------------- writing -------------------------------
# file = open("./data.csv", "w")
# writer = csv.writer(file)
# writer.writerow(["transaction_id", "product_id", "price"])

# file.close()

# writing each row individually
# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerow(["transaction_id", "product_id", "price"])
#     writer.writerow([1000, 1, 5])
#     writer.writerow([1000, 2, 15])

# writing rows in one shot
# with open("data.csv", "w") as file:
#     writer = csv.writer(file)
#     writer.writerows(
#         [["transaction_id", "product_id", "price"], [1000, 1, 5], [1000, 2, 15]]
#     )


#------------------------------------ reading -------------------------------

with open("data.csv", 'r') as file:
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
