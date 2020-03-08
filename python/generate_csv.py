from ENIB_lib import *
import numpy as np

#system
sys = Notch(2,0.9,100)
t,s = sys.step(T=np.linspace(0,0.15,1000))
export_step("../data/data0.csv",t,s)

#system
sys = BP(-5,4,200)
t,s = sys.step(T=np.linspace(0,0.2,1000))
export_step("../data/data1.csv",t,s)

#system6
sys = BP(0.5,0.25,2000)
t,s = sys.step(T=np.linspace(0,0.015,1000))
export_step("../data/data2.csv",t,s)

#system5
sys = HP(4,0.1,100)
t,s = sys.step(T=np.linspace(0,0.6,1000))
export_step("../data/data3.csv",t,s)

# system1
sys = LP(-2,0.2,1000)
t,s = sys.step(T=np.linspace(0,0.06,1000))
export_step("../data/data4.csv",t,s)

#system2
sys = LP(10,2,100)
t,s = sys.step(T=np.linspace(0,0.25,1000))
export_step("../data/data5.csv",t,s)

#system4
sys = HP(10,2,100)
t,s = sys.step(T=np.linspace(0,0.15,1000))
export_step("../data/data6.csv",t,s)

#system7
sys = Notch(10,5,100)
t,s = sys.step(T=np.linspace(0,0.6,1000))
export_step("../data/data7.csv",t,s)

#system7
sys = BP(-5,1,100)
t,s = sys.step(T=np.linspace(0,0.07,1000))
export_step("../data/data8.csv",t,s)

#system3
sys = LP(-1,0.8,500)
t,s = sys.step(T=np.linspace(0,0.016,1000))
export_step("../data/data9.csv",t,s)

#system7
sys = Notch(1,0.05,1000)
t,s = sys.step(T=np.linspace(0,0.12,1000))
export_step("../data/data10.csv",t,s)

