import os
import first_level_cluster_supervised as flc


folders=os.listdir('./merged_feature_file')

# print folders
data_folder='main_feature_file_all_routes'

if data_folder not in os.listdir('./'):
    os.mkdir(data_folder)
            # print "ksdfs"
else:
    flc.clean_directory(data_folder)

fout=open(data_folder+'/'+'main_feature.csv','w')

for index,folder in enumerate(folders):
    if index==0:
        f = open('./merged_feature_file/'+folder+'/'+'feature.csv')
                
        for line in f:
            fout.write(line)
        f.close() # not really needed
    else:
        f = open('./merged_feature_file/'+folder+'/'+'feature.csv')
        f.next() # skip the header
        for line in f:
            fout.write(line)
        f.close() # not really needed
        

fout.close()
    # print type(folder)