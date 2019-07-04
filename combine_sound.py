import os

def convert(s): 
  
    # initialization of string to "" 
    str1 = "" 
  
    # using join function join the list s by  
    # separating words by str1 
    return(str1.join(s)) 

ext="all_extracts"
ext_s="sound_f"
total=os.listdir(ext)
for i in total:
    last_c=[]
    last_c.append(i[(len(i)-2)])
    last_c.append(i[(len(i)-1)])
    c=convert(last_c)
    print(c)
    cmp_l=os.listdir(ext_s)
    for j in cmp_l:
        last_s=[]
        last_s.append(j[(len(j)-6)])
        last_s.append(j[(len(j)-5)])
        s=convert(last_s)
        print(s)
        if c==s:
            os.system("cp "+ext_s+"/"+j +" "+ext+"/"+i)
            
