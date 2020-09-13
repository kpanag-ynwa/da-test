# Design a data structure that

#- Contains aggregated metrics for all insured people 
#    - Total covered amount for all claims
#    - Claims per year
#    - Average age of insured

import pandas as pd
import numpy as np
import uuid

# The Insured class allows to store the attributes of an Insured in an insured object 
class Insured():
    
    # __init__ constructor - lays out the layout of the insured data
    
    def __init__(self):
        
        self.ID= None
        self.name = None
        self.gender = None
        self.date_of_birth = None
        self.age = None
        self.SSN = None
        
    # method that adds an insured individual and brdiges the interface to the back-end. Updates the object with the user's input
    
    def input_to_attributes_insured(self):
        
        self.name = input("What's the name of the insured? ")
        self.gender = input("What's the gender of the insured? ")
        self.date_of_birth = input("What's the date of birth of the insured? ")
        self.age = input("What's the age of the insured? ")
        self.SSN = input("What's the SSN of the insured? ")
        
        return self
    
    # method that returns a unique identifier
    
    def name_to_ID(self,name):
        
        self.ID = '{}-{}'.format(name,uuid.uuid4().hex[:8])
        
        return self.ID
        