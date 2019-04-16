
# 2Pass Loudnorm Implementation

Written by Lawrence Card, implementing the 2 pass loudnorm filter in ffmpeg which was originally developed by Kyle Swanson here: http://k.ylo.ph/2016/04/04/loudnorm.html

This script solves the issue that you have to manually run the loudnorm filter twice and manually enter in the parameters each time for the 2nd pass. This script does that automatically.

Ensure you have Python (3) and ffmpeg installed. ffmpeg.exe can sit in the same folder as this script.

Also ensure you have an 'In' folder and an 'Out' folder in the same directory.

Feel free to remove the loudnormparams.txt file generated in 'Out', this is purley to extract the 2nd pass paramerters and gets regenerated each time you process a file.

## Version Update

V2 loops over all .wav files in the 'In' folder, not just one.

## To Use

Simply install Python3

Then in Command Prompt type:

[path to pyhton interpreter]/python.exe 2Pass_loudnorm_v2.py

Alternatively, add the path to the Python Interpreter as an environment path in Windows, then you can just use 'python.exe' instead of the full path.

Remember to clear out the 'Out' folder before re-running with files of the same name in the 'In' folder (otherwise it gets stuck).