#!/usr/bin/env python

import os
import time
import subprocess
import commands

     ## command to run - return cpu temp(unknown units) ##
cmd_linux = "cat /sys/class/thermal/thermal_zone0/temp "
cmd_linux1 = "date "


     ## run it ##
output = subprocess.check_output(cmd_linux, shell=True)
output1 = subprocess.check_output(cmd_linux1, shell=True)

file = open('temps.csv', 'a')

num_lines = sum(1 for line in open('temps.csv'))
if(num_lines < 1):        
     file.write("\"Date_Time\",\"Temp\"\n")

file.write(output1[:len(output1)-2] + ",")
file.write(output[:5] + "\n")


file.close()
