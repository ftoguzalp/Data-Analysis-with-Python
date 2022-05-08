import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plot
import numpy as np

df=pd.read_csv("radars/Radar_Traffic_Counts.csv")





df=df.drop(columns=['location_name', 'location_latitude', 'location_longitude',
       'Day', 'Day of Week', 'Hour', 'Minute', 'Time Bin',
       'Direction', ])
a=df[(df.Year == 2019) & (df.Month == 1)]
a=int(a.mean()[2])
b=df[(df.Year == 2019) & (df.Month == 2)]
b=int(b.mean()[2])
c=df[(df.Year == 2019) & (df.Month == 3)]
c=int(c.mean()[2])

d=df[(df.Year == 2019) & (df.Month == 4)]
d=int(d.mean()[2])

e=df[(df.Year == 2019) & (df.Month == 5)]
e=int(e.mean()[2])

f=df[(df.Year == 2019) & (df.Month == 6)]
f=int(f.mean()[2])


g=df[(df.Year == 2019) & (df.Month == 7)]
g=int(g.mean()[2])


h=df[(df.Year == 2019) & (df.Month == 8)]
h=int(h.mean()[2])

i=df[(df.Year == 2019) & (df.Month == 9)]
i=int(i.mean()[2])

j=df[(df.Year == 2019) & (df.Month == 10)]
j=int(j.mean()[2])

k=df[(df.Year == 2019) & (df.Month == 11)]
k=int(k.mean()[2])

l=df[(df.Year == 2019) & (df.Month == 12)]
l=l.mean()[2]





Months=["January","February","March","April","May","June","July","August","September","October","November","December"]
Values=[a,b,c,d,e,f,g,h,i,j,k,l]
plot.title("Mean number of vehicles detected by the radar sensors in Austin in 2019")
plot.xlabel("Months")
plot.ylabel("Vehicles")

for i in range (len(Months)):
    plot.text(i,Values[i],Values[i], ha="center",va="bottom")

plot.bar(Months,Values)

plot.show()








# print(f"Mean Volume of year 2017 is {A},mean volume of year 2018 is {B},mean volume of year 2019 is {C}")

# Years=[2017,2018,2019]
# Volumes=[A,B,C]
# plot.bar(Years,Volumes)
# plot.show()