import pandas as pd
import os


def population():
    name='merged_feature_file/trails/feature.csv'
    populate=[]
    population_class=[]
    df=pd.read_csv(name)
    print(len(df))
    l=len(df)
    i=0
    while i<l:
        if df.iloc[i]['zone']=='market' and df.iloc[i]['time_level']==3:
            populate.append('dense')
            population_class.append('3')
        elif df.iloc[i]['zone']=='market' and df.iloc[i]['time_level']==2:
            populate.append('dense')
            population_class.append('3')
        elif df.iloc[i]['zone']=='market' and df.iloc[i]['time_level']==1:
            populate.append('sparse')
            population_class.append('1')
        elif df.iloc[i]['zone']=='market' and df.iloc[i]['time_level']==4:
            populate.append('dense')
            population_class.append('3')
        elif df.iloc[i]['zone']=='highway' and df.iloc[i]['time_level']==3:
            populate.append('medium')
            population_class.append('2')
        elif df.iloc[i]['zone']=='highway' and df.iloc[i]['time_level']==2:
            populate.append('sparse')
            population_class.append('1')
        elif df.iloc[i]['zone']=='highway' and df.iloc[i]['time_level']==1:
            populate.append('sparse')
            population_class.append('1')
        elif df.iloc[i]['zone']=='highway' and df.iloc[i]['time_level']==4:
            populate.append('medium')
            population_class.append('2')
        elif df.iloc[i]['zone']=='normal_city' and df.iloc[i]['time_level']==3:
            populate.append('dense')
            population_class.append('3')
        elif df.iloc[i]['zone']=='normal_city' and df.iloc[i]['time_level']==2:
            populate.append('medium')
            population_class.append('2')
        elif df.iloc[i]['zone']=='normal_city' and df.iloc[i]['time_level']==1:
            populate.append('sparse')
            population_class.append('1') 
        else:
            populate.append('medium')
            population_class.append('2')
       # print("a")
        i+=1
    df['Population_density']=populate
    df['Population_class']=population_class
    print(len(populate))
    df.to_csv(name,index=False)
    cmd="cp "+name+" ./"
    os.system(cmd)

def main():
    #name=["details_54feet_up.csv","details_ukhra_up.csv","details_8B_up.csv","details_azone_up.csv"]
    #for i in name:
    population()


main()

