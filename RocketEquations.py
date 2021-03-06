# RocketEquations
# Written by Brendan

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import ipywidgets as widgets
import time
import math
from IPython.display import display

def ChamberP(pambient,k,M):
    po=pambient*(1+0.5*(k-1)*M**2)**(k/(k-1))
    return po

def ExpansionRatio(k,M):
    ER=(1/M)*((1+0.5*(k-1)*M**2)/(0.5*(k+1)))**((0.5*(k+1))/(k-1))
    return ER

def AreaRatio(k,p2p1):
    AR=((k+1)/2)**(1/(k-1))*(p2p1)**(1/k)*(((k+1)/(k-1))*(1-p2p1**((k-1)/k)))**0.5
    AR=AR**-1
    return AR

def ThroatArea(mdot,p1,R,T1,k):
    At=(mdot/p1)*((R*T1)/(k*(2/(k+1))**((k+1)/(k-1))))**0.5
    return At

def PressureRatio(k,M):
    PPo=((1+0.5*(k-1)*M**2)**(k/(k-1)))**(-1)
    return PPo

def TempRatio(k,M):
    TTo=((1+0.5*(k-1)*M**2))**(-1)
    return TTo

def PropMass(InitialM , FinalM):
    m=InitialM-FinalM
    return m

def MRVehicle(InitialM , FinalM):
    mr=FinalM/InitialM
    return mr

def MRSubSys(InitialM , FinalM , NonSysMass):
    mr=(FinalM-NonSysMass)/(InitialM-NonSysMass)
    return mr

def PMFVehicle(PropellantMass , InitialM):
    PMF=PropellantMass/InitialM
    return PMF

def PMFSubSys(PropellantMass , InitialM , NonSysMass):
    PMF=PropellantMass/(InitialM-NonSysMass)
    return PMF

def MassFlow(ThrustOrPropM , EVelOrBurnTime):
    mflow=ThrustOrPropM/EVelOrBurnTime
    return mflow

def WeightFlow(MFR , gravitySL):  
    WFR=MFR*gravitySL  
    return WFR

def EEV_ISP(Isp , Gravity):
    c=Isp*Gravity
    return c

def EEV_Force(Thrust , MFR):    
    c=Thrust/MFR    
    return c

def IdealThrust(C , MFR):
    F=MFR*C
    return F

def MomThrust(MFR , V2):    
    mt=MFR*V2    
    return mt

def RealThrust(MomentumThrust , PressureThrust):    
    T=MomentumThrust+PressureThrust    
    return T

def TotalImpulse(Force , Time):    
    I=Force*Time   
    return I

def Acceleration(Thrust , Mass):   
    a=Thrust/Mass    
    return a

def CStar(ChamberP , ThroatArea , MFR):    
    cstar=(ChamberP*ThroatArea)/MFR    
    return cstar

def SpecificImpulseT(Thrust , WeightFlowRate):    
    Isp=Thrust/WeightFlowRate    
    return Isp

def SpecificImpulseV(V , SpecGrav):    
    Isp=V/SpecGrav    
    return Isp

def PressThrust(p2 , p3 , A2):    
    pt=(p2-p3)*A2
    return pt

def ExhaustVmass(TotalThrust , PThrust , MFR):
    v=(TotalThrust-PThrust)/MFR
    return v

def ExhaustVMet(k,R,T1,p2p1):
    v=(((2*k)/(k-1))*R*T1*(1-(p2p1)**((k-1)/k)))**(1/2)
    return v

def ExhaustVUS(k,R,ToM,PR):
    v=(((2*k*32.2)/(k-1))*R*ToM*(1-((PR)**-1)**((k-1)/k)))**(1/2)
    return v

def CfIdeal(k,p2p1):
    Cf=(((2*k**2)/(k-1))*(2/(k+1))**((k+1)/(k-1))*(1-(p2p1)**((k-1)/k)))**0.5
    return Cf

def FindEpsln(numbers,eps):   
     numbers = np.asarray(numbers) 
     i=(np.abs(numbers - eps)).argmin() 
     return numbers[i]  
