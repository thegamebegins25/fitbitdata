import matplotlib.pyplot as graph

#raw taken from csv for fitbit ekg data at "waveform_samples -- DO NOT EDIT"
data = ""
data = data[1:-1].split("  ")
print(data)

fdata = []

for i in data:
    fdata.append(int(i))

ax = graph.gca()

ax.get_xaxis().set_visible(False)
graph.plot(fdata)
graph.title('EKG')
graph.xlabel('Readings')
graph.ylabel('data')
graph.show()