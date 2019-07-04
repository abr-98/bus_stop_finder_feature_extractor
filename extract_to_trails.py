import os
import glob

def extract():
    name="all_extracts"
    arr=os.listdir(name)

    arr.sort()

    save_loc="raw_trails"
    if os.path.exists(save_loc):
    	os.system("rm -r "+save_loc)
    os.mkdir(save_loc)

    total_ext=save_loc+"/trails"
    if os.path.exists(total_ext):
    	os.system("rm -r "+total_ext)
    os.mkdir(total_ext)

    for i in arr:
        fle=name+"/"+i
        arr2=os.listdir(fle)
        arr2.sort()
        for j in arr2:
            print(j)
            if 'SOUND' in j:
                fle1=fle+"/"+j
                print(j.split('0')[-1])
                if j.split('0')[-1]=='.txt':
                    ext=j.split('0')[-2]+'0.txt'
                    rename="sound_"+ext
                else:
                    rename="sound_"+j.split('0')[-1]
            
                cmd="mv "+fle1+" "+fle+"/"+rename
                os.system(cmd)
                j=rename
            fle_k=fle+"/"+j
            cmd="cp "+fle_k+" "+total_ext
            os.system(cmd)

def main():
    extract()
main()

            




