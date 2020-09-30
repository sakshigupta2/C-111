import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics
import csv
import random
import pandas as pd 
df = pd.read_csv("School2.csv")
data = df["Math_score"].to_list()
fig = ff.create_distplot([data],["Math Scores"],show_hist = False)
#fig.show()
datamean = statistics.mean(data)
datamedian = statistics.median(data)
datamode = statistics.mode(data)
datastdDev = statistics.stdev(data)
print("Mean, Median, Mode of the data is {} {} {} respectively".format(datamean, datamedian, datamode))
print("Standard Deviation of the data is {}".format(datastdDev))
def randomSetOfMean(counter):
    dataSet = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean
meanlist = []
for i in range(0,1000):
    SetOfMean = randomSetOfMean(100)
    meanlist.append(SetOfMean)
stdDev = statistics.stdev(meanlist)
mean = statistics.mean(meanlist)
firststdDevStart, firststdDevEnd = mean - stdDev, mean + stdDev
secondstdDevStart, secondstdDevEnd = mean - (2*stdDev), mean + (2*stdDev)
thirdstdDevStart, thirdstdDevEnd = mean - (3*stdDev), mean + (3*stdDev)
#fig = ff.create_distplot([meanlist],["Student Marks"],show_hist = False)
#fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17],mode = "lines",name = "Mean"))
#fig.add_trace(go.Scatter(x=[firststdDevStart,firststdDevStart], y=[0,0.17],mode = "lines",name = "Standard Deviation 1 start"))
#fig.add_trace(go.Scatter(x=[firststdDevEnd,firststdDevEnd], y=[0,0.17],mode = "lines",name = "Standard Deviation 1 end"))
#fig.add_trace(go.Scatter(x=[secondstdDevStart,secondstdDevStart], y=[0,0.17],mode = "lines",name = "Standard Deviation 2 start"))
#fig.add_trace(go.Scatter(x=[secondstdDevEnd,secondstdDevEnd], y=[0,0.17],mode = "lines",name = "Standard Deviation 2 end"))
#fig.add_trace(go.Scatter(x=[thirdstdDevStart,thirdstdDevStart], y=[0,0.17],mode = "lines",name = "Standard Deviation 3 start"))
#fig.add_trace(go.Scatter(x=[thirdstdDevEnd,thirdstdDevEnd], y=[0,0.17],mode = "lines",name = "Standard Deviation 3 end"))
#fig.show()
df = pd.read_csv("School_3_Sample.csv")
data = df["Math_score"].to_list()
meanOfSample3 = statistics.mean(data)
print(meanOfSample3)
fig = ff.create_distplot([meanlist],["Fun Sheets"], show_hist = False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0.17],mode = "lines",name = "Mean"))
fig.add_trace(go.Scatter(x=[meanOfSample3, meanOfSample3], y=[0,0.17],mode = "lines",name = "Mean of Sample 3"))
fig.add_trace(go.Scatter(x=[thirdstdDevEnd,thirdstdDevEnd], y=[0,0.17],mode = "lines",name = "Standard Deviation 3 end"))
fig.show()
zScore = (meanOfSample3 - mean)/stdDev
print("Z Score is = ", zScore)