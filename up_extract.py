import os
import pandas as pd

if os.path.exists("input"):
    	os.system("rm -r input")
os.mkdir("input")

folder="all_extracts"
count=0
total=os.listdir(folder)
total.sort()
for i in total:
    count+=1
    fle=folder+"/"+i
    print(fle)
    file_name='input/up_0'+str(count)+".txt"
    print(file_name)
    text=open(file_name,'w')
    #print("a")
    text.write('latitude,longitude,date,time\n')
    text=open(file_name,'a')
    ext=os.listdir(fle)
    for j in ext:
        if 'gps' in j:
            tot_ext=fle+"/"+j
            print(tot_ext)
            df=pd.read_csv(tot_ext)
            #print(df)
            k=0
            #print(len(df))
            while k<len(df):
                #print("A")
                text.write(str(df.iloc[k]['lat'])+","+str(df.iloc[k]['long'])+","+str(df.iloc[k]['date'])+","+str(df.iloc[k]['time'])+"\n")
                k+=1

            text.close()
    


            
