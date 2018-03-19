import subprocess
import os

##V2 loops over all .wav files in the 'In' folder, not just one.

##Written by Lawrence Card, implementing the 2 pass loudnorm filter in ffmpeg which was originally developed by Kyle Swanson here: http://k.ylo.ph/2016/04/04/loudnorm.html
##This script solves the issue that you have to manually run the loudnorm filter twice and manually enter in the parameters each time for the 2nd pass. This script does that automatically.

##Ensure you have Python (3) and ffmpeg installed. ffmpeg.exe can sit in the same folder as this script.
##Also ensure you have an 'In' folder and an 'Out' folder in the same directory.
##Feel free to remove the loudnormparams.txt file generated in 'Out', this is purley to extract the 2nd pass paramerters and gets regenerated each time you process a file.


def twopassloudnorm():

    #Analyse In folder for wavs and create a list
    items = os.listdir("./In")
    fileslist = []

    for file in items:
        if file.endswith(".wav"):
            fileslist.append(file)     

    #Loop over all wavs within In folder
    for wav in fileslist:
            
            #Set the input file and location. Edit as necessary.
            filename = wav 
            fileloc = 'In/'+ filename
            
            #Set the 3 input variables below as desired.
            inputi = -23
            inputtp = -2
            inputlra = 15
            
            #location and name of the parameters txt file generated after the 1st pass
            txtfile = 'Out/'+'loudnormparams' +'.txt'

            print('Loudnorm 1st Pass Processing: '+ fileloc)

            #RUN FIRST LOUDNORM PASS
            subprocess.call(['ffmpeg', '-i', fileloc, '-af', 'loudnorm=I=-23:TP=-2:LRA=15:linear=true:print_format=json', '-f', 'null', '-', '2>', txtfile], shell=True)  

            print('subprocess done')

            #ANALYSE txt FILE TO GET SECOND PASS PARAMETERS        
            #read txt file
            file = open(txtfile, "r")
            lines = file.readlines()
            file.close()

            #####(IS IT TO USE THE OUTPUT OR INPUT PARAMS FOR THE 2nd PASS?)
            #find parameters in txt file
            for line in lines:
                line = line.strip()
                if line.find("output_i")!= -1:
                    ival = line
                    ival = ival.strip('"output_i" : ,')
                if line.find("output_tp")!= -1:
                    tpval = line
                    tpval = tpval.strip('"output_tp" : ,')
                if line.find("output_lra")!= -1:
                    lraval = line
                    lraval = lraval.strip('"output_lra" : ,')
                if line.find("output_thresh")!= -1:
                    threshval = line
                    threshval = threshval.strip('"output_thresh" : ,')
                                
            print(ival)
            print(tpval)
            print(lraval)
            print(threshval)

            #Build 2nd Pass parameters string for loudnorm. This makes it easier to get through the subprocess call
            loudnormparams = 'loudnorm=I='+ str(inputi) +':TP='+ str(inputtp) +':LRA='+ str(inputlra) +':measured_I='+ str(ival) +':measured_LRA='+ str(lraval) +':measured_TP='+ str(tpval) +':measured_thresh='+ str(threshval) +':offset=0.58:linear=true:print_format=summary'

            #Set the output file name and location
            outputfile = 'Out/'+ filename

            print(loudnormparams)

            #RUN SECOND LOUDNORM PASS
            #####(Currently picking up the original input file)
            subprocess.call(['ffmpeg', '-i', fileloc, '-af', loudnormparams, '-ar', '48k', outputfile], shell=True)    

            print('subprocess 2 done')

  
#Run the above function
twopassloudnorm()
print('All Processing Complete')








#Note for V3: output = subprocess.check_output('ffmpeg....', shell=True) .... then parse output instead of generating a txt file?








