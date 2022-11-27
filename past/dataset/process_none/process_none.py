import csv

readfile = csv.reader(open('../offices.csv'))
lines = list(readfile)
lines = lines[1:]
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == '0':
            lines[i][j] = None

print(lines)
fields = ['a','b','c']
filename = 'test.csv'
with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(lines)