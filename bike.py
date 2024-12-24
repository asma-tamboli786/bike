import pandas as pd
import matplotlib .pyplot as plt
df = pd.read_csv('bbike_dataset.csv')
#clean data
df.dropna(inplace=True)
df.drop_duplicates(inplace=True)
print(df)
#calculate avg
avg = df.groupby('company name')['price'].mean()

print("avg price is :",avg)

#plot graph
import matplotlib.pyplot as plt
plt.bar(df['company name'],df['price'],color = 'green',)
plt.xlabel('company name')
plt.ylabel('price')
plt.xticks(rotation=40)
plt.show()

#calculate max and min
max = df.loc[df.groupby('company name')['price'].idxmax()]
print(max[['company name', 'price']])

min = df.loc[df.groupby('company name')['price'].idxmin()]
print(min[['company name', 'price']])

#plot graph cc vs mileage
plt.bar(df['CC'],df['mileage'],color = 'green',)
plt.xlabel('CC')
plt.ylabel('mileage')
plt.xticks()
plt.show()