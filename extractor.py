import pandas as pd
import glob
import os

def extract(name,count):
    arr=os.listdir(name)

   # print(arr)
    ext=name[14:len(name)-4]
    #print(name)
    folder="all_extracts"
    if not os.path.exists("all_extracts"):
    	#os.system("rm -r all_extracts")
        os.mkdir("all_extracts")
    det_folder=folder+"/details_"+ext+"_0"+str(count)
    #print(det_folder)
    if not os.path.exists(det_folder):
	    #os.system("rm -r "+det_folder)
    
        os.mkdir(det_folder)

    ext=ext+".csv"
    ext2=str(count)+'.csv'
    name_g=det_folder+"/gps_"+ext2
    name_w=det_folder+"/wifi_"+ext2
    name_a=det_folder+"/acc_"+ext2
    name_gy=det_folder+"/gyro_"+ext2
    #name_b=det_folder+"/bus_"+ext2
    text=open(name_g,'w')
    text.write('lat,long,date,time\n')
    text.close
    text=open(name_w,'w')
    text.write('mac_id,date,time\n')
    text.close
    text=open(name_a,'w')
    text.write('RSI interface_z,RSI interface_y,RSI interface_x,date,time\n')
    text.close
    text=open(name_gy,'w')
    text.write('Gyro_z,Gyro_y,Gyro_x,date,time\n')
    text.close
    #text=open(name_b,'w')
    #text.close
    text_g=open(name_g,'a')
    text_w=open(name_w,'a')
    text_a=open(name_a,'a')
    text_gy=open(name_gy,'a')
    #text_b=open(name_b,'a')
    fld=name
    
    
    for p in arr:
        #count+=1
        
        
        name_1=fld+"/"+p
        print(name_1)
        text=open(name_1,'r')
        line=text.readlines()[1:]
        #print(line)
        text.close()
        total=[]
        data=[]
        i=0
       # print(len(line))
        if 'LACC' in p or 'GSM' in p or 'bus_rating' in p or 'COM' in p:
            continue
        #if 'GPS' in name:
        #print("d")
        while(i<len(line)):
            #flag=0
            k=line[i].split(',')

            o=0
            while o<len(k):
                if 'GPS' in name_1:
                 #   flag=1
                    if o==4:
                        date,time=k[o].split(' ')
                        data.append(date)
                        data.append(time)
                    else:
                        data.append(k[o])
                if 'ACC' in name_1:
                    if o==3:
                        date,time=k[o].split(' ')
                        data.append(date)
                        data.append(time)
                    else:
                        data.append(k[o])
                if 'WiFi' in name_1:
                    if o==len(k)-1:
                        date,time=k[o].split(' ')
                        data.append(date)
                        data.append(time)
                    else:
                        data.append(k[o])
                if 'GYR' in name_1:
                    if o==3:
                        print(k[o])
                        date,time=k[o].split(' ')
                        data.append(date)
                        data.append(time)
                    else:
                        data.append(k[o])
                o+=1
            #print(str(len(data))+"a")

            total.append(data)
            #print(str(len(total))+"b")
            data=[]
            i+=1
#        print(len(total))
        #print(data)

        if 'GPS' in name_1:
           # print("a")
            i=1

            while(i<len(total)):
                
                #if total[i][5]==total[i-1][5] and total[i][4]==total[i-1][4]:
                    #print("A")
                 #   i+=1
                  #  continue

                #print(comm)
                
                text_g.write(total[i][0]+","+total[i][1]+","+total[i][4]+","+total[i][5]+"\n")
                i+=1
            #text_g.close()
        if 'ACC' in name_1:
           # print("b")
            i=1
        
            while(i<len(total)):
               # print(comm)
                if total[i][3]==total[i-1][3] and total[i][4]==total[i-1][4]:
                    #print("b")
                    i+=1
                    continue
 
                text_a.write(total[i][0]+","+total[i][1]+","+total[i][2]+","+total[i][3]+","+total[i][4]+"\n")
                i+=1
            
            #text_a.close()
        if 'WiFi' in name_1:
           # print("c")
            i=1
            
            while(i<len(total)):
                #if total[i][0]==total[i-1][0] and total[i][len(total[i])-2]==total[i-1][len(total[i])-2] and total[i][len(total[i])-1]==total[i-1][len(total[i])-1]:
                    #print("c")
                  #  i+=1
                 #   continue
 
                
                text_w.write(total[i][0]+","+total[i][len(total[i])-2]+","+total[i][len(total[i])-1])
                i+=1
            
            #text_w.close()
        if 'GYR' in name_1:
           # print("c")
            i=1
            
            while(i<len(total)):
                print(len(total[i]))
                #if total[i][0]==total[i-1][0] and total[i][len(total[i])-2]==total[i-1][len(total[i])-2] and total[i][len(total[i])-1]==total[i-1][len(total[i])-1]:
                    #print("c")
                  #  i+=1
                 #   continue
 
                
                text_gy.write(total[i][0]+","+total[i][1]+","+total[i][2]+","+total[i][3]+","+total[i][4]+"\n")
                i+=1

def main():
    fle='new_data'
    count=0
    arr_2=os.listdir(fle)
    arr_2.sort()
    for i in arr_2:
        count+=1
        fle_name=fle+"/"+i+"/All"
       # print(fle_name)
        extract(fle_name,count)
        
  #  os.system('python3 horn.py')
    os.system('python3 combine_sound.py')
    os.system('python3 up_extract.py')
    '''
    os.system('python3 extract_to_trails.py')
    
    os.system('python clustering.py')
    os.system("python3 weekend_detect.py")
    os.system("python3 population_detect.py")
   # os.system('python3 result_or.py')
    #os.system('python3 match_date.py')'''

main()
