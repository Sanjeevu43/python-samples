import pandas as pd

df = pd.DataFrame({'Date' :['10/2/2011', '11/2/2011', '12/2/2011', '13/2/2011'],
                   'Event' :['Music', 'Poetry', 'Theatre', 'Comedy'],
                    'Cost' :[10000, 5000, 15000, 2000]})

print(df)

df['After Discount'] = df['Cost']-(0.2*df['Cost'])
print(df)

df['After Discount'] = df.apply(lambda each_row: each_row.Cost-(0.1*each_row.Cost),axis=1)
print(df)

