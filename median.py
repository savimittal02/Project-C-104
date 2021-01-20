import csv
with open ("SOCR-HeightWeight.csv",newline = "") as f :
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)
newData = []
for i in range(len(fileData)):
    n = fileData[i][1]
    newData.append(float(n))

l = len(newData)    
total = 0
newData.sort()
if l% 2 == 0:
    m1 = float(newData[l//2])
    m2 = float(newData[l//2-1])
    median= (m1+m2)/2

else :
    median = newData[l//2]

print("median:"  + str(median))

