from faker import Faker
import pandas as pd
import numpy as np

# Instantiate Faker object
fake = Faker()

# Credit card transaction data
card_holder_name = []
card_numner = []
card_expire = []
#card_provider = []
#card_security_code = []
transaction_date = []
transaction_amount = []
address = []

def fake_data(no_of_records):
    for _ in range(no_of_records):
        card_holder_name.append(fake.name())
        card_numner.append(fake.credit_card_number())
        card_expire.append(fake.credit_card_expire())    
        #card_provider(fake.credit_card_provider())
        #card_security_code.append(fake.credit_card_security_code())
        transaction_date.append(fake.date_time_between_dates('-1y', 'now'))
        transaction_amount.append(np.random.randint(2000,9000))
        address.append(fake.address())

# clear previous data
card_holder_name = []
card_numner = []
card_expire = []
transaction_date = []
transaction_amount = []
address = []

fake_data(10)

df = pd.DataFrame(zip(card_holder_name,card_numner,card_expire,transaction_date,transaction_amount,address)
                  ,columns=['CardHolder Name','Card Number','Expire Date','Tran Date','Tran Amount','Address'])
#print(df.head())

df.columns = [column.replace(" ","_")   for column in df.columns]
print(df)
print("==========================================")
#print(df.iloc[:3,[0,1]])
df=df.rename(columns = {'CardHolder_Name':'CardHolderName'})
#print(df.iloc[:2,[0,1]])
#print(df[:1])
print("==========================================")
res = df.query('Tran_Amount > 5000',inplace=False)
print(res.shape)
print(res)
print('******************************************')
print(df)

#print(list(df.columns))