import vpython
from vpython import *

tgraph=graph(xtitle="Time [Days]",ytitle="Number Infected", width=475, height=300)
f1=gcurve(color=color.blue, markers=False)
f2=gcurve(color=color.red)

#number of infected humans at start
N=1

#infection rate - TRY CHANGING THIS
a=.2
a2=.19

#starting time
t=0
#time step
dt=.1
N2=1

#this is a loop for 40 days
while t<45:
 
  #add data to the graph
  
  #update number of infected humans
  N=N+a*N*dt
 
  
  N2=N2+a2*N2*dt
  #update time
  t=t+dt
 
  f1.plot(t,N)
  f2.plot(t,N2)
  
#print("N for a = 0.2 = ",N," people")
#print("N for a = 0.19 = ",N2," people")
print("Difference = ",N-N2," people")
