import pandas as pd
import numpy as np
import uuid

# The data storage class allows to save the insured and claim object all in one place once they are created
class Data_storage():
   
    def __init__(self):
       
        self.insured_list = []
        self.claim_list = []
        self.tot_covered_amount = 0
        self.tot_claims_year = 0
        self.avg_age = 0
       
   
    def display_IDs(self):
       
        IDs = []
        for i in range(0,len(self.insured_list)):
            IDs.append(self.insured_list[i].ID)
           
        return IDs
   
   
    def all_events(self):

        IDN = input("what's the user ID? ")
        events = []
        for i in range(0,len(self.claim_list)):
            if self.claim_list[i].ID == IDN:
                events.append(self.claim_list[i].__dict__)

        return events
   
   
    def combine(self):
        data_dict = [{} for _ in range(0,len(self.claim_list))]

        i = 0

        for k in range(0,len(self.insured_list)):
            for j in range(0,len(self.claim_list)):
                if i <= len(self.claim_list) and self.insured_list[k].ID == self.claim_list[j].ID:
                    data_dict[i].update(self.insured_list[k].__dict__)
                    data_dict[i].update(self.claim_list[j].__dict__)
                    i += 1
        return data_dict
   
    def tot_covered(self):
       
        covered_amount_list = []
        
        for i in self.claim_list:
            covered_amount_list.append(int(i.covered_amount))
            
        self.tot_covered_amount = sum(covered_amount_list)
        
        return self.tot_covered_amount
    
    def tot_claims(self):
       
        claims_list = 0
        
        for i in range(1,len(self.claim_list)+1):
            claims_list += i
            
            
        self.tot_claims_year = claims_list
        
        return self.tot_claims_year
    
    def claim_avg_age(self):
       
        avg_age_list = []
        
        for i in self.insured_list:
            avg_age_list.append(int(i.age))
            
        self.avg_age = sum(avg_age_list)/len(avg_age_list)
        
        return self.avg_age
    
def obj_to_df(df,insured_list):
    df = df.append(insured_list)
    return df