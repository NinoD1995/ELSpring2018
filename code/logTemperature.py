#!/usr/bin/python
import os
import time
import sqlite3 as mydb
import sys
import readTemperature

"""
	Log Current Time, Temperature in Celsius and Fahrenheit 
	To an Sqlite3 database 
"""

def logTemp():
     con = mydb.connect('/home/pi/Embedded_Linux/ELSpring2018/code/temperature.db')
     with con: 
          try:
               [t,C,F] = readTemperature.readTemp()
               print "Current temperature is %s F" %F
               cur = con.cursor()
               cur.execute('CREATE TABLE IF NOT EXISTS TempData(date_time TEXT, tempF REAL, tempC REAL)')
               #sql = 'insert into TempData values(?,?,?)', (t,C,F))
               print "Temperature logged!"
               con.commit()
               cur.close()
          except: print "Error!!"

     con.close()
print readTemperature.readTemp()
logTemp()
