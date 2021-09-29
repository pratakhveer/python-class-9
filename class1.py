import csv
from os import read
import pandas as pd
import plotly.express as px

with open("class1.csv", newline="") as f:
    reader = csv.reader(f)
    fileData = list(reader)

fileData.pop(0)

mark = 0
totalEntries = len(fileData)

for marks in fileData:
    mark = mark + float(marks[1])

mean = mark/totalEntries
print("the means is :"+str(mean))

df = pd.read_csv("class1.csv")
fig = px.scatter(df, x="Student Number", y="Marks")
fig.update_layout(shapes=[
    dict(type="line", y0=mean, y1=mean, x0=0, x1=totalEntries)
])

fig.show()
