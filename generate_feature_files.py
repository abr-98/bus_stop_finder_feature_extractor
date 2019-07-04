import os
import sys
import csv
import first_level_cluster as flc
from lib import *
import datetime

# import pandas as pd


# def comp(a):
#     """comparison function to sort the file_names lexicographically.... eg, up_1 comes before up_2"""
#     # print a
#     # a= a.split('_')
#     # # print a
#     # a= int(a[1].split('.')[0])
#     # print a
#     return a   
def compareTime(time1,time2):
    for i in range(len(time1)):
        if time1[i]!=time2[i]:
            return 0
    return 1


def dayOfWeek(day, month, year):
    t= [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    year = year- (month < 3)
    return ( year + year/4 - year/100 + year/400 + t[month-1] + day) % 7 
# def getWifiData
class generateFeatureFiles():

    def __init__(self,DATA_FOLDER,INPUT_FOLDER):
        self.files=[]
        self.fileDict={}
        self.data_folder=DATA_FOLDER
        self.input_data_folder=INPUT_FOLDER
        self.zone={'market_place':{'lat':'23.5631833333','lng':'87.28356'},'normal_city':{'lat':'23.5440616667','lng':'87.2887366667'},'highway':{'lat':'23.4946766667','lng':'87.3168283333'}}
        self.wifi_file_names_data={}
        self.sound_file_names_data={}

    def store_dict(self):
        # print a
        self.files=os.listdir(self.data_folder)
        for file in self.files:
            # print file
            a=file
            a= a.split('_')
            # print a
            trail_number= int((a[1].split('.'))[0])
            # print trail_number
            fileType=a[-1].split('.')[0]
            # print fileType

            if trail_number in self.fileDict:
                pass
            else:
                self.fileDict[trail_number]={}

            # if(fileType == "groups"):
            #     self.fileDict[trail_number]['local_group']=file
            if(fileType == "leader"):
                self.fileDict[trail_number]['local_group_leader']=file
                # print fileDict[trail_number]

                self.fileDict[trail_number]['trail_number']=trail_number
            
        
        # //===============wifi files name data======================//
        files=os.listdir(self.input_data_folder)
        # print files

        for f in files:
            a=f.split('_')
            # print a
            if a[0]=='wifi':
                trail=a[1].split('.')[0]
                # print trail
                self.wifi_file_names_data[trail]=f
            # fileObj[trail]=f
            # print trail

        # //===============wifi files name data======================//
        files=os.listdir(self.input_data_folder)
        # print files

        for f in files:
            a=f.split('_')
            # print a
            if a[0]=='sound':
                trail=a[1].split('.')[0]
                # print trail
                self.sound_file_names_data[trail]=f

            # print a
        # return a

    def getWifiData(self,row):
        # [lat,long,date,time,count,trail_no,local_group_no,starting_leader_time,distance,timelevel,zone,day]
        # [lat,long,date,time,count,trail_no,local_group_no,starting_leader_time,ending_time,distance,timelevel,zone,day]
        trail_no=row[5]
        
        start_time=row[7]  # starting_leader_point
        start_time = [int(i) for i in start_time.split(':')]
        count=int(row[4])
        h=start_time[0]
        m=start_time[1]
        s=start_time[2]
        starting_seconds=int(datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds())
        
        ending_time=row[8]  # ending_time_for_group
        ending_time = [int(i) for i in ending_time.split(':')]
        count=int(row[4])
        h=ending_time[0]
        m=ending_time[1]
        s=ending_time[2]
        ending_seconds=int(datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds())
        # print time
        filename=self.wifi_file_names_data[trail_no]
        file=open(self.input_data_folder+'/'+filename,'r')
        data= file.read().splitlines()
        data=data[1:]
        

        mylist=[]
        for line in data:
            line=line.split(',')
            t=line[-1]
            t = [int(i) for i in t.split(':')]
            # print line
            seconds=int(datetime.timedelta(hours=int(t[0]),minutes=int(t[1]),seconds=int(t[2])).total_seconds())
            if(seconds>=starting_seconds and seconds <=ending_seconds):
                # append mac address
                mylist.append(line[0])
            elif seconds>ending_seconds:
                break
        
        total_wifi=len(set(mylist))
            
            # print t
            # if(t)
            # break
        # print data
        # print count
        row.append(total_wifi)

    def getSoundData(self,row):
        # [lat,long,date,time,count,trail_no,local_group_n      o,starting_leader_time,distance,timelevel,zone,day]
        THRESHHOLD=65
        trail_no=row[5]
        
        start_time=row[7]  # starting_leader_point
        start_time = [int(i) for i in start_time.split(':')]
        count=int(row[4])
        h=start_time[0]
        m=start_time[1]
        s=start_time[2]
        starting_seconds=int(datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds())
        
        ending_time=row[8]  # ending_time_for_group
        ending_time = [int(i) for i in ending_time.split(':')]
        count=int(row[4])
        h=ending_time[0]
        m=ending_time[1]
        s=ending_time[2]
        ending_seconds=int(datetime.timedelta(hours=int(h),minutes=int(m),seconds=int(s)).total_seconds())
        # print time
        print(trail_no)
        filename=self.sound_file_names_data[trail_no]
        file=open(self.input_data_folder+'/'+filename,'r')
        data= file.read().splitlines()
        data=data[1:]
        

        total_count=0
        for line in data:
            line=line.split(',')
            t=line[1]
            # print line
            t = [int(i) for i in t.split(':')]
            seconds=int(datetime.timedelta(hours=int(t[0]),minutes=int(t[1]),seconds=int(t[2])).total_seconds())
            if(seconds>=starting_seconds and seconds <=ending_seconds):
                # append mac address
                # print float(line[-1])
                if float(line[-1]) > THRESHHOLD :
                    # print "hey"
                    total_count=total_count+1
            elif seconds>ending_seconds:
                break
            # print t
            # if(t)
            # break
        # print data
        # print count
        row.append(total_count)




    def createFeatureFile(self):
        if 'feature_folder' not in os.listdir('.'):
            os.mkdir('feature_folder')
        else:
            pass
            # flc.clean_directory('feature_folder')
        data_sub_folder=self.data_folder.split('/')[-1]
        # print data_sub_folder

        if data_sub_folder not in os.listdir('./feature_folder'):
            os.mkdir('./feature_folder/'+data_sub_folder)
            # print "ksdfs"
        else:
            flc.clean_directory('./feature_folder/'+data_sub_folder)
            # print data_sub_folder ," dir cleaned"


        for trail_number in self.fileDict:
            # local_group_file_name=self.fileDict[trail_number]['local_group']
            local_group_leader_file_name=self.fileDict[trail_number]['local_group_leader']
            
            # local_group_file= open(self.data_folder+'/'+local_group_file_name,'r')
            local_group_leader_file= open(self.data_folder+'/'+local_group_leader_file_name,'r')

            # temp1= csv.reader(local_group_file)
            temp2= csv.reader(local_group_leader_file)
            
            # localGroup=[]
            localGroupLeader=[]
            
            fields=temp2.next()
            fields.append('next_stop_distance')
            # print fields

            # for row in temp1: 
            #     localGroup.append(row)
                # print row 
            # print temp2
            # temp2.next()
            for row in temp2:
                localGroupLeader.append(row)
                # print row      

            # //========================add next stop distance=================//
            # temp_distance= 0
            for index,row in enumerate(localGroupLeader):
                # lat=float(row[0])
                # lng=float(row[1])
                # grp_no=int(row[-1])

                # found=False
                # for r in localGroup:
                #     lat_2=float(r[0])
                #     lng_2=float(r[1])
                #     grp_no_2=int(r[-1])
                #     if lat==lat_2 and lng==lng_2 and grp_no == grp_no_2:
                #         r.append("1")
                #         found=True
                #         break

                # if found == False:
                #     print "not found for lat: ",lat,"long ",lng,"grp_no ",grp_no
                # print row[0]
                
                
                if index < len(localGroupLeader)-1:
                    distance=get_spherical_distance(localGroupLeader[index][0],localGroupLeader[index+1][0],localGroupLeader[index][1],localGroupLeader[index+1][1])
                    # temp_distance+=distance
                    row.append(str(distance))
                    
                else:
                    # print temp_distance
                    # temp_distance=str(float(temp_distance/(len(localGroupLeader)-1)))
                    # print temp_distance
                    row.append(localGroupLeader[index-1][-1])
                    # print "sadfas"

            # for row in localGroup:
            #     if len(row)==6:
            #         row.append("0")

            # for i in localGroup:
            #     print i[-2]," ",i[-1]
            


            # ========================add the time level feature=============================//
            fields.append("time_level")
            for row in localGroupLeader:
                time=row[3]
                time = [int(float(j)) for j in time.split(':')]
                # print time
                # break
                if time[0]>=5 and time[0]<=8:
                    row.append("1")
                elif time[0]>=9 and time[0]<=12:
                    row.append("2")
                elif time[0]>=13 and time[0]<=16:
                    row.append("3")
                elif time[0]>=17 and time[0]<=22:
                    row.append("4")


            # ===========================add the zone feature=================================//
            fields.append("zone")
            for row in localGroupLeader:
                lat=row[0]
                lng=row[1]
                zone=self.zone
                m_dist=get_spherical_distance(lat,zone['market_place']['lat'],lng,zone['market_place']['lng'])
                n_dist=get_spherical_distance(lat,zone['normal_city']['lat'],lng,zone['normal_city']['lng'])
                h_dist=get_spherical_distance(lat,zone['highway']['lat'],lng,zone['highway']['lng'])
                min_dist=min(m_dist,n_dist,h_dist)
                if(min_dist==m_dist):
                    row.append("market_place")
                elif min_dist==n_dist:
                    row.append("normal_city")
                elif min_dist==h_dist:
                    row.append("highway")
            

            # //==============================add the day========================================//
            fields.append("Day")
            for row in localGroupLeader:
                date=row[2]
                date=date.split('/')
                # month / day / year
                # print (int(date[0]))
                day=dayOfWeek(int(date[1]),int(date[0]),int(date[2]))
                if(day==0):
                    row.append('Sunday')
                elif(day==1):
                    row.append('Monday')
                elif(day==2):
                    row.append('Tuesday')
                elif(day==3):
                    row.append('Wednesday')
                elif(day==4):
                    row.append('Thursday')
                elif(day==5):
                    row.append('Friday')
                elif(day==6):
                    row.append('Saturday')
                # break

            # //==============================add the wifi data===============================//
            
            # [lat,long,date,time,count,trail_no,local_group_no,starting_local_leader_time,distance,timelevel,zone,day]
            fields.append('wifi_count')
            for row in localGroupLeader:
                self.getWifiData(row)
                # # print row
                # break

            # //==============================add the wifi data===============================//
            fields.append('honks')
            for row in localGroupLeader:
                self.getSoundData(row)


            


            output_file=open('feature_folder/'+data_sub_folder+'/'+str(trail_number)+'_feature.csv', 'wb')
            csvWriter = csv.writer(output_file)
            csvWriter.writerow(fields)
            csvWriter.writerows(localGroupLeader)

            # break




            # local_group_file = pd.read_csv(self.data_folder+'/'+local_group_file_name)
            # local_group_leader_file = pd.read_csv(self.data_folder+'/'+local_group_leader_file_name)

    def mergeFeatureFile(self):
        if 'merged_feature_file' not in os.listdir('.'):
            os.mkdir('merged_feature_file')
        else:
            pass
            # flc.clean_directory('merged_feature_file')

        data_sub_folder=self.data_folder.split('/')[-1]
        # print data_sub_folder

        if data_sub_folder not in os.listdir('./merged_feature_file'):
            os.mkdir('./merged_feature_file/'+data_sub_folder)
            # print "ksdfs"
        else:
            flc.clean_directory('./merged_feature_file/'+data_sub_folder)
            # print data_sub_folder ," dir cleaned"


        files = os.listdir('./feature_folder/'+data_sub_folder)
        # print files
        fout=open('merged_feature_file/'+data_sub_folder+'/'+'feature_without_groundtruth.csv','wb')

        for index,file in enumerate(files):
            if index==0:
                f = open('./feature_folder/'+data_sub_folder+'/'+file)
                
                for line in f:
                    fout.write(line)
                f.close() # not really needed
            else:
                f = open('./feature_folder/'+data_sub_folder+'/'+file)
                f.next() # skip the header
                for line in f:
                    fout.write(line)
                f.close() # not really needed
        
        fout.close()


    def setGroundTruth(self,GROUNDTRUTH_FILE):
        
        data_sub_folder=self.data_folder.split('/')[-1]

        fout=open('merged_feature_file/'+data_sub_folder+'/'+'feature_without_groundtruth.csv','r')
        ground_truth=open(GROUNDTRUTH_FILE,'r')
        
        f= csv.reader(fout)
        gt= csv.reader(ground_truth)

        gt_list=[]
        fout_list=[]

        fields=f.next()
        fields.append("bus_stop")

        length=len(fields)

        for i in f:
            fout_list.append(i)
        
        gt.next()

        for i in gt:
            gt_list.append(i)

        # print gt_list

        for row in gt_list:
            lat=(row[0])
            lng=(row[1])
            for row2 in fout_list:
                lat2=(row2[0])      
                lng2=(row2[1])
                
                distance=get_spherical_distance(lat,lat2,lng,lng2)
                if(distance<15):
                    row2.append("1")
        

        for row in fout_list:
            if len(row)!=length:
                row.append("0")

        
        output_file=open('merged_feature_file/'+data_sub_folder+'/'+'feature.csv', 'wb')
        csvWriter = csv.writer(output_file)
        csvWriter.writerow(fields)
        csvWriter.writerows(fout_list)


    
def main(DATA_FOLDER,INPUT_FOLDER,GROUNDTRUTH_FILE):
    featGenerator=generateFeatureFiles(DATA_FOLDER,INPUT_FOLDER)
    
    featGenerator.store_dict()
    # sorted(files,key=comp)
    sorted(featGenerator.fileDict)
    # # for key in featGenerator.fileDict:
    # #     print featGenerator.fileDict[key]['trail_number']
    # # #     print featGenerator.fileDict[key]['local_group']
    # #     print featGenerator.fileDict[key]['local_group_leader']
    
    
    featGenerator.createFeatureFile()
    featGenerator.mergeFeatureFile()
    featGenerator.setGroundTruth(GROUNDTRUTH_FILE)
    # for i in files:
    #     print i
