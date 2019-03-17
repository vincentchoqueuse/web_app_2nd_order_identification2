import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

system_list=[]
E_list=[1,4,10,3,-2,1]

# system1
K=2
w0=10000
m=0.5
system1 = signal.lti([K], [(1/(w0**2)),2*m/w0,1])
system_list.append(system1)

#system2
K=-5
w0=100
m=0.8
system2 = signal.lti([K], [(1/(w0**2)),2*m/w0,1])
system_list.append(system2)

#system3
K=0.2
w0=300
m=0.05
system3 = signal.lti([K], [(1/(w0**2)),2*m/w0,1])
system_list.append(system3)

#system4
K=2
wc=1000
m=0.1
system4 = signal.lti([K], [1/wc,1])
system_list.append(system4)

#system5
K=-10
w0=2000
m=0.7
system5 = signal.lti([K], [(1/(w0**2)),2*m/w0,1])
system_list.append(system5)

#system6
K=-10
w0=1000
m=2
system6 = signal.lti([K], [(1/(w0**2)),2*m/w0,1])
system_list.append(system6)

for indice in range(len(system_list)):
    E = E_list[indice]
    system=system_list[indice]
    t,s=system.step(N=500)
    e = E*np.ones(len(t))
    filename="../data/data{}.csv".format(indice)
    header="t, e, s"
    data=np.transpose([t,e,E*s])
    np.savetxt(filename,data,header=header, delimiter=",",comments="")
