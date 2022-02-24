import csv

lines = [
        {'name': 'Маша', 'age': 25, 'job': 'Scientist'}, 
        {'name': 'Вася', 'age': 8, 'job': 'Programmer'}, 
        {'name': 'Эдуард', 'age': 48, 'job': 'Big boss'},
    ]

with open('export.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['name','age','job'])
    for line in lines:
        writer.writerow(line)


        
