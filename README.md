# da-test
Groundspeed Analytics Take Home Challenge

```

This project entails the creation of a data schema where a user can add an insured and claim level data

The backbone of the code consist of OOP for the datastructure and manipulation, and pandas dataframes for data storage.
```

# Code Structure
More about the dataframe, classes and methods:


#### Dataframe
Schema = Df that stores: attributes of insured and claim:

```
'claim_number','name','ID','gender','date_of_birth','SSN','smoking_status','allergies',\
'medical_conditions', 'loss_date','issue_type','billed_amount','covered_amount'
```

#### Classes

```

Insured() - Class that stores all of the insureds attributes and the input_to_attributes_insured and name_to_ID methods.

Claim() - Class that stores all of the claim attributes and the input_to_attributes_claim method.

Data_storage() - Class that stores all of the combined insured/claim attributes and other methods.
```
#### Go to the Interface Section

#### Import packages and the Classes from the Package module by running:

```
import pandas as pd
import numpy as np
import uuid

from Package.insured import Insured
from Package.claim import Claim
from Package.data import Data_storage,obj_to_df
```
#### Run the schema dataframe section of the code and initialize the Data Storage object. 


```
schema = pd.DataFrame(columns=['claim_number','name','ID','gender','date_of_birth','SSN','smoking_status',\
                               'allergies','medical_conditions','loss_date', 'issue_type', 'billed_amount'])
```

```
data_storage = Data_storage()
```

The Interface is designed to take inputs from the user and store the inputs in the objects themselves

#### Add an insured individual and return the unique identifier of that individual by running the cell below

```
insured = Insured()

insured.input_to_attributes_insured()

print(insured.name_to_ID(insured.name))

data_storage.insured_list.append(insured)
```
#### Add an insurance event for a specific user identified by unique identifier by running the cell below
```
claim = Claim()

claim.input_to_attributes_claim()

print(claim.claim_number)

data_storage.claim_list.append(claim)
```
#### List all insureds by running
```
data = data_storage

data.display_IDs()
```
#### List all events associated with a specific user by unique identifier by running
```
events = data.all_events()
events
```
#### Combine insured data with claim data by running
```
combined_data = data.combine()
combined_data
```
#### Save data in the schema by running
```
temp = obj_to_df(schema,combined_data)
print("Great the insured's biodata and claim data have been stored:")
temp
```
