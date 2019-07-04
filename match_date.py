import os
import pandas as pd
import csv
import glob
def convert(s): 
  
    # initialization of string to "" 
    str1 = "" 
  
    # using join function join the list s by  
    # separating words by str1 
    return(str1.join(s)) 

if os.path.exists("details_new"):
	os.system("rm -r details_new")
os.system("python clustering.py")
k="details/up_"
os.mkdir("details_new")
p=".txt_local_group_leader.csv"
r=".txt_local_group_leader.txt"

l=34
i=1
while i<l:
	
	i_s=str(i)
	n=k+"0"+i_s+r
	cmd="cp "+n+" details_new/"
	#print(cmd)
	os.system(cmd)
	cmd="mv details_new/up_0"+i_s+r+" "+"details_new/up_0"+i_s+p
	#print(cmd)
	os.system(cmd)
	i+=1

fle="total_details.csv"
#name='details_final.csv'
if os.path.exists(fle):
	os.system("rm -r total_details.csv")

path='details_new/'
all_files=glob.glob(os.path.join(path,"*_local_group_leader.csv"))

df_from_each_file=(pd.read_csv(f)for f in all_files)
concatenated_df=pd.concat(df_from_each_file,ignore_index=True)

concatenated_df.to_csv(fle,index=False)


ext2="all_extracts"

#arr=os.listdir(ext)
arr2=os.listdir(ext2)


#    print(fle)
df=pd.read_csv(fle)
date=[]
i=0
while i<len(df):

    for j in arr2:
 #       print(j)
        
        
            fle2=ext2+"/"+j
            
            main_arr=os.listdir(fle2)
            for k in main_arr:
                if 'gps' in k:

                    
                    fle2=fle2+"/"+k
  #                  print(fle2)
                    df2=pd.read_csv(fle2)
                    #print("d")
                    p=0
                    
                    while p<len(df2):
                            #print(df2.iloc[p][3])
                            if df.iloc[i][2]==df2.iloc[p][3]:
                                date.append(df2.iloc[p]['date'])
                                print("a")
                                break
                            p+=1
                        #print(date)
    i+=1
print(date)
df['date']=date
df.to_csv(fle,index=False)
    

                    
            

