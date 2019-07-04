import first_level_cluster
#import second_level_cluster
#import new_groundtruth
import get_feature_file_2
import sys
import os
#import read_config

threshold_fp_fn={}

INPUT_FILE = 'raw_trails/trails'
OUTPUT_FOLDER = 'output'
GROUND_TRUTH = 'ground_truth/54feet.txt'
DISTANCE_THRESHOLD = 15
TIME_START = '05:00:00'
TIME_END = '22:00:00'
THRESHOLD =10
TRAIL_ID_RANGE = 34
GROUND_TRUTH_THRESHOLD =50
FP_DISTANCE = 100

#INPUT_FILE,OUTPUT_FOLDER,GROUND_TRUTH,DISTANCE_THRESHOLD,TIME_START,TIME_END,THRESHOLD, TRAIL_ID_RANGE,GROUND_TRUTH_THRESHOLD, FP_DISTANCE \
#= read_config.read_config()
input_files=['./raw_trails/trails']
ground_truth_files=['ground_truth/54feet.txt']
# input_files=['input/GPS_Trails/up_8B','input/GPS_Trails/up_azone','input/GPS_Trails/up_54feet','input/GPS_Trails/up_ukhra']
# ground_truth_files=['./groundtruth/8B_GT_SS(1) (copy).txt','groundtruth/azone.txt','groundtruth/54feet.txt','groundtruth/ukhra_new.txt']
# input_files=['input/GPS_Trails/up_8B','input/GPS_Trails/up_azone','input/GPS_Trails/up_54feet','input/GPS_Trails/up_ukhra']
# ground_truth_files=['groundtruth/8B_GT_SS.txt','groundtruth/azone.txt','groundtruth/54feet.txt','groundtruth/ukhra_new.txt']
# input_files=['input/GPS_Trails/up_azone','input/GPS_Trails/up_54feet','input/GPS_Trails/up_ukhra']
# ground_truth_files=['groundtruth/azone.txt','groundtruth/54feet.txt','groundtruth/ukhra_new.txt']

# input_files=['input/GPS_Trails/up_54feet','input/GPS_Trails/up_ukhra']
# ground_truth_files=['groundtruth/54feet.txt','groundtruth/ukhra_new.txt']

for ind,f in enumerate(input_files):
    local_groups,num_trails= first_level_cluster.main(input_files[ind],DISTANCE_THRESHOLD,TIME_START,TIME_END,TRAIL_ID_RANGE)  #both arguments are directories (input and output, respectively)

    print "Num trails: ",num_trails

    # create a feature file for each of the trail


    # generate_feature_files.main();



    data_sub_folder=f.split('/')[-1]

    # print data_sub_folder



    DATA_FOLDER='./output_data/'+data_sub_folder
    get_feature_file_2.main(DATA_FOLDER,input_files[ind],ground_truth_files[ind])
    # generate_feature_files_local_leader.main(DATA_FOLDER,GROUND_TRUTH)



