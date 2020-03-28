import pandas as pd 
import numpy as np


df=pd.read_csv('feature.csv')

#print(len(df))

#TRain
X=df[['zone','time_level','next_stop_distance','total_waiting_time','wifi_count','honks','Population_density','rsi_z','rsi_y','rsi_x','gyro_z','gyro_y','gyro_x','Weekend/day','Signal','bus_stop','Turn']].values
X_d=pd.DataFrame(X,columns=['zone','time_level','next_stop_distance','total_waiting_time','wifi_count','honks','Population_density','rsi_z','rsi_y','rsi_x','gyro_z','gyro_y','gyro_x','Weekend/day','Signal','bus_stop','Turn'])
#X_d=pd.DataFrame(X)


#y=df[['bus_stop','latitude','longitude']].values
'''y_d=pd.DataFrame(y)
y_d_2=pd.get_dummies(y_d)

X_train, X_test, y_train_k, y_test_k = train_test_split(X_d,y_d,test_size=0.2,random_state=42)
#print(X_train)
y_train1=y_train_k[0].copy()
y_train=pd.DataFrame(y_train1)
y_test1=y_test_k[0].copy()
y_test=pd.DataFrame(y_test1)

#l=len(y_test_k)
#i=0
lat=y_test_k[1].copy()
lat_l=lat.tolist()

long=y_test_k[2].copy()
long_l=long.tolist()
    

X_train_2=pd.get_dummies(X_train,columns=[0,1,6,8])
#X_train_2[1] = X_train_2[1].astype(float)

#y_train_2=pd.get_dummies(y_train)
X_test_2=pd.get_dummies(X_test,columns=[0,1,6,8])
#X_test_2[1] = X_test_2[1].astype(float)'''
df2=pd.get_dummies(X_d,columns=['zone','time_level','Population_density','Weekend/day'])

df2.to_csv('features_embedded.csv',index=False)
