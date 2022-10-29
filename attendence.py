filename = 'Q4/attendance.txt'
with open(filename) as fh:
    l = 1
    b = []
    a = fh.readlines()
    a[0] = (a[0])[1:]
    for i in range(0, len(a), 2):
        a[i] = (a[i])[:-9]  # Remove timestamps and /n
        a[i + 1] = a[i + 1].replace('-', '') # Remove hyphens
        a[i + 1] = a[i + 1].lower() # change the comment posted to lower case
        a[i + 1] = a[i + 1].replace('present', '') # remove present from the comment
        a[i + 1] = a[i + 1].replace(' ', '') # remove spaces from the comment
        if i != len(a) - 2:
            a[i + 1] = (a[i + 1])[:-1] # remove /n from the comment except for last comment 
        b.append([a[i], a[i + 1]]) # Builld a list with elements as ['Name','Roll no.']
    
    # below code is to ceate a new file A.txt and write the content of the attendance 
    # list b in clea and uniform way
    txt = ''
    for q in b:
        q = " ".join(q)
        txt=txt+q+'\n'
    file1 = open("Q4/A.txt","w")
    file1.write(txt[:-1])


import csv
CSVfile = open('Q4/reference.csv')
csvreader = csv.reader(CSVfile)
header = next(csvreader)
rows = []
for row in csvreader:
    rows.append(row)
for x in rows:
    roll_no = x[1]
    if x[2] == 'VANKAYALAPATI SAI VENKATA SATWIK':
        x[2] = 'Satwik Vankayalapati'  # change name of satwik since it are different in atendance.txt and reference.csv
    name = x[2].lower()
    for lines in b:
        if roll_no in lines[1] and lines[0].lower() not in name and name not in lines[0].lower(): 
            # above condition if for some one name is not complete in refrence .csv or in
            print (lines[0] + ' proxied for ' + name + ' Roll no. ' + roll_no) 
            # above condition prints the name from attendance.txt who proxied the attendance and for whom.

CSVfile.close()
