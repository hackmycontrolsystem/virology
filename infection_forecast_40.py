#Estimate of new infections for 40 days
import vpython
from vpython import *

tgraph=graph(xtitle="Time [Days]",ytitle="Number Infected", width=475, height=300)
f1=gcurve(color=color.blue, markers=False)

#number of infected humans at start
N=1

#infection rate - TRY CHANGING THIS
a=.2

#starting time
t=0
#time step
dt=.1

#this is a loop for 40 days
while t<45:
  #add data to the graph
  f1.plot(t,N)
  #update number of infected humans
  N=N+a*N*dt
  #update time
  t=t+dt
  
#Source: https://www.wired.com/story/how-fast-does-a-virus-spread/
