import csv 

FILENAME = "users.csv"

users = [
    ["Mike", 15],
    ["Kevin", 21],
    ["Bob", 34],
    ["Cellesta", 25]
]

with open(FILENAME, "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(users)

with open(FILENAME, "a", newline="") as file:
    users = ["Herald", 18]
    writer = csv.writer(file)
    writer.writerow(users)