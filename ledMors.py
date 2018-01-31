# import modules
import RPi.GPIO as GPIO
import time

pin = 11 

    
def main():
    #to use Raspberry Pi board pin numbers
    GPIO.setmode(GPIO.BOARD)
    # set up GPIO output channel
    GPIO.setup(pin, GPIO.OUT)

    mesaj = input("Mesajınız : ")
    morsText = morsEncoder(mesaj)
    print(morsText)
    morsToLight(morsText)
    GPIO.cleanup()
    

def ledYak(state,value):
    if(state == "Up"):
      GPIO.output(pin,GPIO.HIGH)
      time.sleep(value)
      GPIO.output(pin,GPIO.LOW)
      
    elif(state == "Down"):
      GPIO.output(pin,GPIO.LOW)
      time.sleep(value)
      
    return


def morsEncoder(mesaj):
    convertedText = ""
    alfabe ={
        "A" : ".-",
        "B" : "-...",
        "C" : "-.-.",
        "D" : "-..",
        "E" : ".",
        "F" : "..-.",
        "G" : "--.",
        "H" : "....",
        "I" : "..",
        "J" : ".---",
        "K" : "-.-",
        "L" : ".-..",
        "M" : "--",
        "N" : "-.",
        "O" : "---",
        "P" : ".--.",
        "Q" : "--.-",
        "R" : ".-.",
        "S" : "...",
        "T" : "-",
        "U" : "..-",
        "V" : "...-",
        "W" : ".--",
        "X" : "-..-",
        "Y" : "-.--",
        "Z" : "--..",
        " " : "/",
        "1" : ".----",
        "2" : "..---",
        "3" : "...--",
        "4" : "....-",
        "5" : ".....",
        "6" : "-....",
        "7" : "--...",
        "8" : "---..",
        "9" : "----.",
        "0" : "-----"
        }
  
    var1 = mesaj.upper()
    for x in var1[:]:
        convertedText += alfabe[x]+" "
    
    return convertedText
  
def morsToLight(param):
  helper = {
    "." : 0.08,
    "-" : 0.3,
    " " : 0.3,
    "/" : 1
  }
  
  for x in param[:]:
    if( x == "." or x == "-"):
      #light up
      ledYak("Up",helper[x])
      ledYak("Down",helper[" "])
    else:
      ledYak("Down",helper[x])
    
while True:
    try:
        main()
    except KeyboardInterrupt:
        ledYak("Down",0.01)
        GPIO.cleanup()
        print('Program Sonlandırıldı')
        exit()