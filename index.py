import csv
#opening reference file and creating list of header
CSVfile = open('reference1.csv')
csvreader = csv.reader(CSVfile)
head = next(csvreader)
print(head)
head[0].split('\\')
print(head[0])
header = ['a','a','a','a']
take = ""
count = 0
for x in head[0]:
    if(x=='\t'):
        header[count] = take
        count = count + 1
        take = ""
    else:
        take += x
header[count] = take
take = ""
print(header)
print('\n')
rows = []
count1=0
#Creating a list of reference file
for row in csvreader:
    row1 = ['a','a','a','a']
    count = 0

    for x in row[0]:
        # print(x)
        if(x=='\t'):
            row1[count] = take
            count = count + 1
            take = ""
        else:
            take += x
    row1[count] = take
    take = ""
    rows.append(row1)

links = []
with open("url.txt", "a") as f:
    for x in rows:
        f.writelines('https://www.amazon.'+ x[3] +'/dp/'+ x[2] + "\n")
        links.append('https://www.amazon.'+ x[3] +'/dp/'+ x[2])

print(links)

CSVfile.close()
