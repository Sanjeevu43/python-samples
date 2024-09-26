from faker import Faker
import pandas as pd
import numpy as np
from sklearn.datasets import make_classification, make_regression

name = "Suhana Khan"

fake = Faker(['en_IN'])
df = pd.DataFrame(
    [
        {
             "name": fake.name(),
             "card_number": fake.credit_card_number(),
             "card_expire": fake.credit_card_expire(),    
             "transaction_date": fake.date_time_between_dates('-1y', 'now'),
             "transaction_amount": np.random.randint(2000,9000),
             "address": fake.address(),
             "email": fake.email()
        }
        for _ in range(10)
    ]
)
print(df)

df1 = pd.DataFrame(
    [
        {
             "ULD_BUILD_SPL_ID":np.random.randint(1,99999),
             "ULD_BUILD_ID": np.random.randint(1,99999),
             "SPECIAL_HANDLING_CODES_ID": np.random.randint(1,126),    
             "SPL_SEQUENCE_NUM": 0,             
        }
        for _ in range(10)
    ]
)
print(df1)
