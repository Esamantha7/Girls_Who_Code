import pandas
from datetime import datetime
import matplotlib.pyplot as plt

data = pandas.read_csv("weather_year.csv")

#

#print (len(data))


data.columns=["EDT","maxTemp","meanTemp","minTemp","maxDew","meanDew","minDew",
              "maxHum","meanHum","minHum","maxSeaPress","meanSeaPress",
              "minSeaPress","maxVis","meanVis","minVis","maxWindSpeed","meanWindSpeed",
              "maxGustSpeed","precip","cloudCov","events","windDirDegree"]
###print (data.columns)
###print (data.maxVis.head(20))
###print(data.EDT.head())
##first_EDT = data.EDT.values[0]
###print (first_EDT)
##
##fD = datetime.strptime(first_EDT, "%Y-%m-%d")
##print(fD)
###datetime.EDTtime(2012, 3, 10, 0, 0)
##
##data.EDT = data.EDT.apply(lambda d: datetime.strptime(d, "%Y-%m-%d"))
##print (data.EDT.head())
##
####data.index = data.EDT
####print (data)
##
##data = data.drop(["EDT"], axis=1)
##print (data.columns)
##
##empty = data.apply(lambda col: pandas.insull(col))
##print(empty)

plt.xlabel("Day")
plt.ylabel("Day in Farenheit")
plt.title("Day vs. Temp")

plt.hist(data.minTemp, color="red")
plt.hist(data.minHum, color="purple")
plt.grid(True)
plt.show()
