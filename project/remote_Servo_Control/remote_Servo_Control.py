from __future__ import division
import time

# Import the PCA9685 module.
import Adafruit_PCA9685
from flask import Flask, render_template, request



app = Flask(__name__)
@app.route('/')
def hello():
     return render_template('testServo_1.html')

@app.route('/',methods=['POST'])
def PrintData():
    if request.method=='POST':
        # Uncomment to enable debug output.
        #import logging
        #logging.basicConfig(level=logging.DEBUG)

        # Initialise the PCA9685 using the default address (0x40).
        pwm = Adafruit_PCA9685.PCA9685()

        # Alternatively specify a different address and/or bus:
        #pwm = Adafruit_PCA9685.PCA9685(address=0x41, busnum=2)

        # Configure min and max servo pulse lengths
        servo_min = 150  # Min pulse length out of 4096
        servo_max = 600  # Max pulse length out of 4096

        # Helper function to make setting a servo pulse width simpler.
        def set_servo_pulse(channel, pulse):
            pulse_length = 1000000    # 1,000,000 us per second
            pulse_length //= 60       # 60 Hz
            print('{0}us per period'.format(pulse_length))
            pulse_length //= 4096     # 12 bits of resolution
            print('{0}us per bit'.format(pulse_length))
            pulse *= 1000
            pulse //= pulse_length
            pwm.set_pwm(channel, 0, pulse)

         # Set frequency to 60hz, good for servos.
        pwm.set_pwm_freq(60)
        print('Moving servo on channel 0, press Ctrl-C to quit...')
         
        servoPosition=int(request.form['servoControl'])
        
        print('Servos are turning\n')
        pwm.set_pwm(0, 0, servoPosition)
        time.sleep(1)
        pwm.set_pwm(0, 0, 600)
        time.sleep(1)
        print('servos are done turning\n')

        #pwm.set_pwm(1, 0, servoPosition)
        #time.sleep(1)
        
    return render_template('testServo_1.html')




if __name__ == "__main__":
     app.run(host='0.0.0.0', port=80, debug=True)