import pandas as pd
import plotly.express as px
import csv

with open("class2.csv", newline="") as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)

totalEntries = len(fileData)

mark = 0

for marks in fileData:
    mark = mark + float(marks[1])

mean = mark/totalEntries

print("mean is:"+str(mean))

df = pd.read_csv("class2.csv")
fig = px.scatter(df, x="Student Number", y="Marks")

fig.update_layout(shapes=[
    dict(type="line", y0=mean, y1=mean, x0=0, x1=totalEntries)
])
fig.update_yaxes(rangemode="tozero")
fig.show()
