import csv

with open("ww2_countries.csv") as csvfile:
  csvreader = csv.reader(csvfile)
  for row in csvreader:
    print(row[1])
