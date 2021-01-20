import csv
from collections import Counter

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

data = Counter(newData)
modeDataforRange = {
    "50-60":0,
    "60-70":0,
    "70-80":0,
}

for Heigth , occurence in data.items():
    if 50<float(Heigth)<60 : modeDataforRange["50-60"] += occurence
    elif 60<float(Heigth)<70 : modeDataforRange["60-70"] += occurence
    elif 70<float(Heigth)<80 : modeDataforRange["70-80"] += occurence

modeRange , modeOccerence = 0,0
for range , occurence in modeDataforRange.items():
    if occurence>modeOccerence:
        modeRange,modeOccerence = [int(range.split("-")[0]), int(range.split("-")[1])]

mode=float((modeRange[0]+modeRange[1])/2)        
        
print(f"mode:{mode : 2f}")