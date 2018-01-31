import RPi.GPIO as GPIO
import time

class LedYak:

    def __init__(self, pin, time, status): #LedYak(11,0.5,UP)  gpio 11 voltage high
        
        self.pin = pin
        self.time = time
        self.status = status
        
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(self.pin, GPIO.OUT)

        if self.time is 'Null':
            CheckStatus(self.status)
        else:
            self.CheckStatus(self.status)
            self.SleepTime(self.time)
            self.led_down()
            self.SleepTime(self.time)

    def CheckStatus(self,statu):
        if statu.upper() == 'UP':
            return self.led_up()
        elif statu.upper() == 'DOWN':
            return self.led_down()
            
    def led_up(self):
       return GPIO.output(self.pin,True)

    def led_down(self):
       return GPIO.output(self.pin,False)

    def SleepTime(self,value):
       return time.sleep(value)
    
