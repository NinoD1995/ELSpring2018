#!/usr/bin/env python

import os
import time
import subprocess
import commands

     ## command to run - return cpu temp(unknown units) ##
cmd_linux = "cat /sys/class/thermal/thermal_zone0/temp "

     ## run it ##
output = subprocess.check_output(cmd_linux, shell=True)
file = open('temps.csv', 'a')

num_lines = sum(1 for line in open('temps.csv'))
if(num_lines < 1):        
     file.write("\"Temp\"\n")

file.write(output[:5] + "\n")
file.close()
