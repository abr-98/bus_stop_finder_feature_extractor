import pandas as pd
import os
from math import *

def get_spherical_distance(lat1,lat2,long1,long2):
        """
        Get spherical distance any two points given their co-ordinates (latitude, longitude)
        """
        # print lat1," ", lat2," ",long1," ",long2
        # print type(lat1)," ", type(lat2)," ",type(long1)," ",type(long2)
        # print type(lat1)," ", type(lat2)," ",type(long1)," ",type(long2)
        # print type(long1)," ",type(long2)
        # print float(long1)," ",float(long2)
        lat1,lat2,long1,long2= float(lat1),float(lat2),float(long1),float(long2)
        q=radians(lat2-lat1)
        r=radians(long2-long1)
        lat2r=radians(lat2)
        lat1r=radians(lat1)
        a=sin(q/2)*sin(q/2)+cos(lat1r)*cos(lat2r)*sin(r/2)*sin(r/2)
        c=2*atan2(sqrt(a),sqrt(1-a))
        R=6371*1000
        d=R*c
        return d

def signal():
    signal1=[]
    signal2=[]
    signal=[]
    name='feature.csv'
    name2='signal/Signal_1.csv'
    name3='signal/Signal_2.csv'
    df=pd.read_csv(name)
    df1=pd.read_csv(name2)
    df2=pd.read_csv(name3)

    l1=len(df1)
    l2=len(df2)


    l=len(df)
    i=0
    while i<l:
        signal1.append(0)
        signal2.append(0)
        i+=1
    k=0
   # k=int(k)
    while k<l1:
        if 'Signal' in str(df1.iloc[k]['Signal']):
            print(str(df1.iloc[k]['Signal']))
            j=0
            while j<l:
                if get_spherical_distance(df.iloc[j]['latitude'],df1.iloc[k]['lat'],df.iloc[j]['longitude'],df1.iloc[k]['long'])<30:
                    if signal1[j]==0:
                        signal1[j]=1
                
                j+=1
            print("Epoch1 Complete")
        k+=1
    print("1 done")
    k=0
    while k<l2:
        if 'Signal' in str(df2.iloc[k]['Signal']):
            print(str(df2.iloc[k]['Signal']))
            j=0
            while j<l:
                if get_spherical_distance(df.iloc[j]['latitude'],df2.iloc[k]['lat'],df.iloc[j]['longitude'],df2.iloc[k]['long'])<30:
                    if signal2[j]==0: 
                        signal2[j]=1
                
                j+=1
            print("Epoch2 Complete")
        k+=1
    z=0
    while z<l:
        if signal1[z]==1 or signal2[z]==1:
            signal.append(1)
        else:
            signal.append(0)


        z+=1
    df['Signal']=signal
    #df['Population_class']=population_class
    df.to_csv(name,index=False)

def main():
    #name=["details_54feet_up.csv","details_ukhra_up.csv","details_8B_up.csv","details_azone_up.csv"]
    #for i in name:
    signal()


main()


                
