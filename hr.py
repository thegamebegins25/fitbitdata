import matplotlib.pyplot as graph
import matplotlib.dates as mdates
import json
import os
import datetime
import numpy as np

x = []
y = []

files = os.listdir("json")
for fname in files:
    #print(fname)
    fname = "json/" + fname
    file = open(fname, "r")
    data = file.read()
    data = json.loads(data)
    #print(data)
    for i in data:
        #print(i)
        y.append(i.get("value").get("bpm"))
        dt = i.get("dateTime")
        dt = datetime.datetime.strptime(dt, "%m/%d/%y %H:%M:%S")
        x.append(dt)
        
    file.close()

dates = mdates.date2num(x)
width = np.diff(dates).min()

fig, ax = graph.subplots()
ax.xaxis_date()
fig.autofmt_xdate()

graph.plot(dates, y)
graph.title('Total Heart Rate')
graph.xlabel('Date/Time')
graph.ylabel('bpm')
graph.show()