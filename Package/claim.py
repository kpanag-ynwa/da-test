import pandas as pd
import numpy as np
import uuid

# The Claim class allows to store the attributes of a claim in a claim object 
class Claim():
   
    def __init__(self):
       
        self.ID = None
        self.smoking_status = None
        self.allergies = None
        self.medical_conditions = None
        self.loss_date = None
        self.issue_type = None
        self.billed_amount = None
        self.covered_amount = None
        self.claim_number = None
       
    def input_to_attributes_claim(self):
       
        self.ID = input("what's the user ID? ")
        self.smoking_status = input("what's the smoking status of the user? ")
        self.allergies = input("what are the allergies of the user? ")
        self.medical_conditions = input("what are the medical conditions of the user? ")
        self.loss_date = input("what's the loss date of the claim? ")
        self.billed_amount = input("what's the billed amount of the claim? ")
        self.covered_amount = input("what's the covered amount of the claim? ")
        self.claim_number = 'claim-{}'.format(uuid.uuid4().hex[:8])
       
        return self