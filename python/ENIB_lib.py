import numpy as np
from scipy.signal import lti


def export_step(filename,t,s):
    header="t, s"
    data=np.transpose([t,s])
    np.savetxt(filename,data,header=header, delimiter=",",comments="")


def export_bode(filename,w,mag,phase):
    header="w, module, argument"
    data=np.transpose([w,mag,phase])
    np.savetxt(filename,data,header=header, delimiter=",",comments="")

class TF():

    def __init__(self):
        pass

    def sys(self):
        pass

    def Q(self):
        return 1/(2*self.m)
    
    def wp(self):
        return self.wn*np.sqrt(1-2*self.m**2)
    
    def Tp(self):
        wp = self.wn*np.sqrt(1-2*self.m**2)
        return 2*np.pi/wp

    def freqresp(self,w=None):
        sys = self.sys()
        w,Tjw = sys.freqresp(w)
        return w,Tjw

    def bode(self,w=None):
        w,Tjw = self.freqresp(w=w)
        mag = np.abs(Tjw)
        phase = 180*np.angle(Tjw)/np.pi
        return w, mag,phase

    def step(self,T=None):
        sys = self.sys()
        t,s = sys.step(T=T)
        return t,s


class LP(TF):

    def __init__(self,T0,m,w0):
        self.T0 = T0
        self.m = m
        self.w0 = w0

    def wr(self):
        return self.w0*np.sqrt(1-2*self.m**2)

    def sys(self):
        num = [self.T0]
        den = [1/(self.w0**2),2*self.m/self.w0,1]
        return lti(num,den)

class HP(TF):

    def __init__(self,Too,m,w0):
        self.Too = Too
        self.m = m
        self.w0 = w0

    def wr(self):
        return 1/(self.w0*np.sqrt(1-2*self.m**2))
    
    def sys(self):
        num = [self.Too/(self.w0**2),0,0]
        den = [1/(self.w0**2),2*self.m/self.w0,1]
        return lti(num,den)

class BP(TF):

    def __init__(self,Tm,m,w0):
        self.Tm = Tm
        self.m = m
        self.w0 = w0
    
    def sys(self):
        num = [2*self.m*self.Tm/(self.w0),0]
        den = [1/(self.w0**2),2*self.m/self.w0,1]
        return lti(num,den)

class Notch(TF):

    def __init__(self,T0,m,w0):
        self.T0 = T0
        self.m = m
        self.w0 = w0
    
    def sys(self):
        num = [self.T0/(self.w0**2),0,self.T0]
        den = [1/(self.w0**2),2*self.m/self.w0,1]
        return lti(num,den)


