#!/usr/bin/env python
# coding: utf-8

# In[89]:


import numpy as np
import math

class investment:
    
        
    def __init__(self,rf_return,rf_risk,risk_aversion):
        
        self.list_return = []
        self.list_weight = []
        self.rf_return = rf_return
        self.rf_risk = rf_risk
        self.risk_aversion = risk_aversion
            
    
    def add_return(self,*expect_return):
        
               
        for i in expect_return:
            
            if type(i) == str: raise TypeError("Expect integer but str")
            self.list_return.append(i)
            
    def add_weight(self,*weight):
        
        if len(self.list_return) == 0: raise Warning("Input return first")        
        if len(self.list_return) != len(weight): raise Warning("Length of return and weight is not same")
        if sum(weight) != 1: raise Warning("Sum of weight should be 1")
        for j in weight:
            if type(j) == str: raise TypeError("Expect integer but str")
            self.list_weight.append(j)
    
    def get_return(self):
        
        return self.list_return
    
    def get_weight(self):
        
        return self.list_weight
        
    def update(self,update_return,*update_weight):
        
        self.list_return.append(update_return)
        self.list_weight = []
        
        
        check = 0
        for i in update_weight:
            self.list_weight.append(i)
            check +=i
        
        if len(self.list_return) != len(self.list_weight) : raise Warning("Length of return and weight is not same")
        if check != 1 : raise Warning("Sum of weight should be 1")
        
        
    
    def p_return(self):
        
        np1 = np.array(self.list_return)
        np2 = np.array(self.list_weight)
        
        p_return = np.dot(np1,np2)      
        
        return p_return
    

    
    def deviation(self):
        
        result = []
        
        for k in self.list_return:
            result.append((self.p_return() - k)**2)
        
        return result
    
    def variance(self):
        
        np1 = np.array(self.list_weight)
        np2 = np.array(self.deviation())
        
        return np.dot(np1,np2)
    
    def sqd(self):
        
        return math.sqrt(self.variance())
    
    def utility(self):
        
        if len(self.list_return) == 0 or len(self.list_weight) == 0 : raise Warning("list_return or list_weight is empty") 
        
        return self.p_return()-1/2*self.risk_aversion*self.sqd()
        


# In[ ]:




