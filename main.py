import csv

with open("YA_Books.csv", mode = "r", encoding="utf-8") as file:
    books = csv.reader(file)

    for row in books:
        print(row)