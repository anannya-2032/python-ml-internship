import csv
with open("file.csv", "r") as f:
    reader_object = csv.reader(f)
    for line in reader_object:
        print(line)