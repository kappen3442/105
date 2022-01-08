import csv
with open("class2.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)
    filedata.pop(0)
    totalmarks=0
    totalentries=len(filedata)
    for i in filedata:
        totalmarks+=float(i[1])
    print(totalmarks)