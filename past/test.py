import csv
fields = ['a','b','c']
filename = 'test.csv'
readfile = csv.reader(open('test.csv'))
lines = list(readfile)
lines = lines[1:]
for i in range(len(lines)):
    for j in range(len(lines[0])):
        if lines[i][j] == '3':
            lines[i][j] = None
print(lines)

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(lines)