import pandas as pd
import os


def weekend():
    name='merged_feature_file/trails/feature.csv'
    week=[]
    #population_class=[]
    df=pd.read_csv(name)
    print(len(df))
    l=len(df)
    i=0
    while i<l:
        if df.iloc[i]['Day']=='Sunday' or df.iloc[i]['Day']=='Saturday':
            week.append('Week-end')
             
        else:
            week.append('Week-day')
            #population_class.append('2')
       # print("a")
        i+=1
    df['Weekend/day']=week
    
    print(len(week))
    df.to_csv(name,index=False)
    #cmd="cp "+name+" ./"
    #os.system(cmd)

def main():
    #name=["details_54feet_up.csv","details_ukhra_up.csv","details_8B_up.csv","details_azone_up.csv"]
    #for i in name:
    weekend()


main()

