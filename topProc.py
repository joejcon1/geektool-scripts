#! /usr/bin/python
import subprocess
import os
import re
RED = "\033[1;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
DEFAULT="\033[0;39m"

On_Black='\033[37m'       # Black
On_Red='\033[31m'         # Red
On_Green='\033[42m'       # Green
Color_Off='\033[0m'    


command = ["ps", "-arcwwwxo command %cpu"]
child = subprocess.Popen(command, stdout=subprocess.PIPE)
complete = child.communicate()
procs = re.findall('(?<=\n)\w+[ ]*\w+[ ]*\w+[ ]*\w+[ ]*[0-9]*.[0-9]*', complete[0] )


for x in range(10):
	tuples = procs[x].split()
	score = tuples[len(tuples)-1]
	name = tuples[0]
	if(float(score) > 15.0):
		print On_Red + '{:<17} {:>10}'.format(name, score)
	else:
		print On_Black + '{:<17} {:>10}'.format(name, score)
	
