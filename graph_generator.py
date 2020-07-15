import pandas as pd
import os
import matplotlib.pyplot as plt
from os import listdir
from os.path import isfile, join


mypath = r'C:\Users\... \Monitoring'
fileslist = [f for f in listdir(mypath) if isfile(join(mypath, f))]
listfiledate = []
l_sod_totalGB = []
sod02_02_TotalDataCapacity, sod02_01_TotalDataCapacity, sod01_01_TotalDataCapacity, sod01_02_TotalDataCapacity = ([] for i in range(4))
sod02_02_UsedData, sod02_01_UsedData, sod01_01_UsedData, sod01_02_UsedData = ([] for i in range(4))
sod02_02_AvailableData, sod02_01_AvailableData, sod01_01_AvailableData, sod01_02_AvailableData = ([] for i in range(4))
usedbar02_02, bar02_01, bar01_01, bar01_02 = ([] for i in range(4))
availablebar02_02 = []
#l_sod_name = ['sod02_02_highperformance', 'sod02_01_highperformance', 'sod01_02_highperformance', 'sod01_01_highperformance']
l_sod_name = []
l_usedbar, l_availablebar = ([] for i in range(2))
latest_file = fileslist[-1]


for file in fileslist:
    filename = os.path.splitext(join(mypath, file))[0]
    filedate = filename.split("_")[2]
    listfiledate.append(filedate)
    data = pd.read_csv(join(mypath, file))
    df1 = pd.DataFrame(data, columns = ['Aggregate', 'Total Data Capacity (GB)', 'Used Data Capacity (GB)', 'Used Data %', 'Available Data Capacity (GB)', 'Available Data %', 'Daily Growth Rate %'])
    datalist = df1.values.tolist()
    for i in range(0, 4):
        sod_name = datalist[i][0]
        sod_TotalDataCapacity = datalist[i][1]
        sod_UsedData = datalist[i][2]
        sod_AvailableData = datalist[i][4]
        if i == 0:
            sod02_02_TotalDataCapacity.append(sod_TotalDataCapacity)
            sod02_02_UsedData.append(sod_UsedData)
            sod02_02_AvailableData.append(sod_AvailableData)
        if i == 1:
            sod02_01_TotalDataCapacity.append(sod_TotalDataCapacity)
            sod02_01_UsedData.append(sod_UsedData)
            sod02_01_AvailableData.append(sod_AvailableData)
        if i == 2:
            sod01_01_TotalDataCapacity.append(sod_TotalDataCapacity)
            sod01_01_UsedData.append(sod_UsedData)
            sod01_01_AvailableData.append(sod_AvailableData)
        if i == 3:
            sod01_02_TotalDataCapacity.append(sod_TotalDataCapacity)
            sod01_02_UsedData.append(sod_UsedData)
            sod01_02_AvailableData.append(sod_AvailableData)
    if file == latest_file:
        for i in range(0,4):
            l_sod_name.append(datalist[i][0])
            l_usedbar.append(datalist[i][2])
            l_availablebar.append(datalist[i][4])
            if i == 0:
                usedbar02_02 = datalist[i][2]
                availablebar02_02 = datalist[i][4]
            if i == 1:
                bar02_01 = [datalist[i][2], datalist[i][4]]
            if i == 2:
                bar01_01 = [datalist[i][2], datalist[i][4]]
            if i == 3:
                bar01_02 = [datalist[i][2], datalist[i][4] ]

plt.subplot(3, 2, 1)
plt.title('Free GB per Aggregate')
plt.xlabel('Date')
plt.ylabel('Available Data (GB)')
plt.plot(listfiledate, sod02_02_AvailableData, color='lightgreen', linestyle='dashed', linewidth=2,
         marker='o', markerfacecolor='green', markersize=6, label="Available Data sod02_02")
plt.plot(listfiledate, sod02_01_AvailableData, color='green', linestyle='dashed', linewidth=2,
         marker='o', markerfacecolor='green', markersize=6,label ="Available Data sod02_01")
plt.plot(listfiledate, sod01_02_AvailableData,  color='lightblue', linestyle='dashed', linewidth=2,
         marker='o', markerfacecolor='blue', markersize=6, label="Available Data sod01_02")
plt.plot(listfiledate, sod01_01_AvailableData, color='blue', linestyle='dashed', linewidth=2,
         marker='o', markerfacecolor='blue', markersize=6, label="Available Data sod01_01")
plt.legend()

plt.subplot(3, 2, 2)
plt.title('Used GB per Aggregate')
plt.xlabel('Date')
plt.ylabel('Consumed Data (GB)')
plt.plot(listfiledate, sod02_02_UsedData, color='lightgreen', linestyle='dashed', linewidth=2,
         marker='o', markerfacecolor='green', markersize=6, label="Used Data sod02_02")
plt.plot(listfiledate, sod02_01_UsedData, color='green', linestyle='dashed', linewidth=2,
         marker='o', markerfacecolor='green', markersize=6, label="Used Data sod02_01")
plt.plot(listfiledate, sod01_02_UsedData,  color='lightblue', linestyle='dashed', linewidth=2,
         marker='o', markerfacecolor='blue', markersize=6, label="Used Data sod01_02")
plt.plot(listfiledate, sod01_01_UsedData, color='blue', linestyle='dashed', linewidth=2,
         marker='o', markerfacecolor='blue', markersize=6, label="Used Data sod01_01")
plt.legend()

plt.subplot(3, 2, 3)
p1 = plt.barh(l_sod_name, l_usedbar, color='red')
p2 = plt.barh(l_sod_name, l_availablebar, left=l_usedbar, color='limegreen')


plt.subplot(3, 2, 4)
plt.title('Total Used TB vs Total Available TB')
labels = ["%.2f" % round(sum(l_usedbar)/1024, 2), "%.2f" % round(sum(l_availablebar)/1024, 2)]
explode = (0, 0.1, 0, 0)
p = plt.pie(labels, labels=labels, autopct='%1.1f%%', colors=('red','limegreen'),
        shadow=True, startangle=90)

plt.subplot(3, 2, 5)
plt.title('DC1 - Total Used TB vs Total Available TB')
labels = ["%.2f" % round((l_usedbar[2] + l_usedbar[3])/1024, 2), "%.2f" % round((l_availablebar[2] + l_availablebar[3])/1024, 2)]
explode = (0, 0.1, 0, 0)
p = plt.pie(labels, labels=labels, autopct='%1.1f%%', colors=('red','limegreen'),
        shadow=True, startangle=90)

plt.subplot(3, 2, 6)
plt.title('DC2 - Total Used TB vs Total Available TB')
labels = ["%.2f" % round((l_usedbar[0] + l_usedbar[1])/1024, 2), "%.2f" % round((l_availablebar[0] + l_availablebar[1])/1024, 2)]
explode = (0, 0.1, 0, 0)
p = plt.pie(labels, labels=labels, autopct='%1.1f%%', colors=('red','limegreen'),
        shadow=True, startangle=90)

plt.show()
