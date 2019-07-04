import os
from math import *
import datetime

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


def get_group_leader(group):
        """ returns the group_leader point for a particular group of points"""
       
        if group == []:
            return
        wait_per_distance= [] #contains the summation of wait_time/distance from one point to all other point, for every point in the group
        total_wait_time=0  #would contain the total wait time of the group, we sum up the 'count' field of all the points

        for each_point in group:
            wait_time= int(each_point[4])  #each_point= [latitude,longitude,date,timestamp,count,trail_no,local_group_number]
            temp=0   #temp would contain wait_time* (1/d1 + 1/d2 + 1/d3 + .....) where d1,d2,d3...dn are distances from one point to all other points
            for other_point in group:
                #get distance from each_point to other_point, d1,d2,d3.... etc
                distance= get_spherical_distance(float(each_point[0]),float(other_point[0]),float(each_point[1]),float(other_point[1]))
                temp+= 1/(distance+1)  # here, temp= (1/d1 + 1/d2 + 1/d3 + .....)
            temp= wait_time*temp        #now, temp= wait_time* (1/d1 + 1/d2 + 1/d3 + ....)
            wait_per_distance.append(temp)  #append temp to the list
            total_wait_time+=wait_time 
        
        max_index=0

        max_wait_per_distance= max(wait_per_distance) #get the maximum value from the list
 
        #get the index of the point having maximum wait_per_distance
        for index in xrange(0,len(wait_per_distance)):
           if max_wait_per_distance == wait_per_distance[index]:
               max_index= index
               break
        
        # import datetime
        
        # starting_time=group[0][3]
        # ending_time=group[-1][3]
        # t = [int(i) for i in starting_time.split(':')]
        # seconds1=int(datetime.timedelta(hours=int(t[0]),minutes=int(t[1]),seconds=int(t[2])).total_seconds())
        # t= [int(i) for i in ending_time.split(':')]
        # seconds2=int(datetime.timedelta(hours=int(t[0]),minutes=int(t[1]),seconds=int(t[2])).total_seconds())

        # if total_wait_time== seconds2+group[-1][4]-seconds1:
        #     print "error"
        #     print group[0][-2]
            # global c+=1
            # print c

        group_ending_time=group[-1][3]
        t= [int(i) for i in group_ending_time.split(':')]
        seconds=int(datetime.timedelta(hours=int(t[0]),minutes=int(t[1]),seconds=int(t[2])).total_seconds())
        seconds=  seconds+int(group[-1][4])
        end_time=str(datetime.timedelta(seconds=seconds))

        group[max_index][4]= total_wait_time  #replace 'count' field with total_wait_time.
        group[max_index].append(group[0][3]) #[timestamp] starting time
        group[max_index].append(end_time) #[timestamp] ending time

        return group[max_index]  #return the group leader point