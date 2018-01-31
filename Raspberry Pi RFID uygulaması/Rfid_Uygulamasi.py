import RPi.GPIO as GPIO
from Rfid_Oku import *
from LedYak import *

GPIO.setwarnings(False)

PassesCards=[]

def main():
    print('Kart Okutunuz, Led ,Dogru Kart Okundugunda uzun, \n yanlis kartta 2kere kisa yanacaktir')
    with open ("PassCards.txt", "r") as Cardfile:
        data = Cardfile.read()
        PassesCards.append(data.split('\n'))
        print('Kart Bekleniyor')
        
def islem(card):
    if card in PassesCards[0]:
        print ('Kart izni Var')
        LedYak(11,2,'UP')
        GPIO.cleanup()
    else:
        print('Kart izni Yok')
        LedYak(11,0.2,'UP')
        LedYak(11,0.2,'UP')
        GPIO.cleanup()
main()
while(True):
    try:
        durum = Rfid_Oku.oku() 
        if durum is not None:
            GPIO.cleanup()
            print('Kart Algilandi')
            Card = str(Rfid_Oku.oku())
            print (Card)
            islem(Card)
            print('Kart Bekleniyor')
        else:
            print('Kart Bekleniyor')
            
    except KeyboardInterrupt:
        GPIO.cleanup()
        print('Program Sonlandırıldı')
        exit()
            
    finally:
        GPIO.cleanup()


