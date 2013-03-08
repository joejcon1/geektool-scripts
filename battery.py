#! /usr/bin/python
import subprocess
import re
import os

RED = "\033[1;31m"
GREEN = "\033[0;32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
DEFAULT="\033[0;39m"

On_Black='\033[40m\033[1;30m'       # Black
On_Red='\033[41m\033[1;31m'         # Red
On_Green='\033[42m\033[32m'       # Green
Color_Off='\033[0m'    

command = ["pmset", "-g", "batt"]


child = subprocess.Popen(command, stdout=subprocess.PIPE)
complete = child.communicate()
m = re.search('([0-9]*%)', complete[0] )

percentage = m.group(0)
percentage = percentage[0:-1]
percentage = int(percentage)
output = ''


for x in range(100):
	if (100-x < int(percentage)):
		if(int(percentage) > 25):
			color = On_Green
		else:
			color = On_Red
	else:
		color = On_Black
	
	output += "\n" + color+'|'+ On_Black 

print output