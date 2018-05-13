<img src="https://www.newpaltz.edu/media/identity/logos/newpaltzlogo.jpg" width="300">

# Spring 2018 Embedded Linux class
This repository documents my class work and projects done for **CPS342**
1. **Personal Information:**

   Name: *Minh Nguyen* 
   
   Major: *Computer Engineering*  
   
   ID: *[N03097188](https://github.com/N03097188)*  
   
   Year: *Senior*
   
2. **Class Start Date:** Jan 22, 2018
3. **Class End Date:** May 8, 2018

**Project Participation**

*Anthony DiNardi: 60%*

*Minh Nguyen: 30%*

*Dean: 0%*





This repository focuses on the servo side of the the IOT security camera using a raspberry pi. This includes setting up the hardware as well as the software side of the project reguarding the servos. 

Materials gathered to motorize the IOT security camera are 2 SG5010, PCA9685, and sevaeral jumper cables. First, connect the two servos to channel 0 and channel 1 of the servo driver. Next, solder a DC barrel connector to the power line of the servo driver. Once this is done, a standard DC power cable will be sufficient to power the servos. Next the driver was interfaced with the Pi. Connect the VCC to a 3.3v power supply on the raspberry pi and connect GND on the driver to GND on the raspberry pi. Then connect the SCLK of the driver to the SCL1 pin on the rapsberry pi, and also, hook up the SDA pin from the driver to the SDA1 pin on the rapberry pi. At this point the hardward side of the IOT security camera pertain to motorized movements are complete. For the software side of the servos, refer to the folder "code." 
