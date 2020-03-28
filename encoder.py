import pandas as pd

df=pd.read_csv('feature.csv')
population_class=[]
zone_class=[]
week=[]
l=len(df)

for i in range(0,l):
    if df.iloc[i]['zone']=='highway':
        zone_class.append(0)
    if df.iloc[i]['Population_density']=='dense':
        population_class.append(0)
    if df.iloc[i]['Weekend/day']=='Week-day':
        week.append(0)
    if df.iloc[i]['zone']=='normal_city':
        zone_class.append(1)
    if df.iloc[i]['Population_density']=='medium':
        population_class.append(1)
    if df.iloc[i]['Weekend/day']=='Week-end':
        week.append(1)
    if df.iloc[i]['zone']=='market_place':
        zone_class.append(2)
    if df.iloc[i]['Population_density']=='sparse':
        population_class.append(2)

df['Population_class']=population_class
df['zone_class']=zone_class
df['week_class']=week

name='feature.csv'
df.to_csv(name,index=False)
