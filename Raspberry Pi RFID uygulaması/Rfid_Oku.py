from pirc522 import RFID
import signal
import time

class Rfid_Oku:
    def oku():
        rdr = RFID()
        util = rdr.util()
        util.debug = True

        rdr.wait_for_tag()
        (error, data) = rdr.request()
        
        if not error:
            #print("Kart Algilandi!")
            (error, uid) = rdr.anticoll()
            if not error:
                kart_uid = str(uid[0])+" "+str(uid[1])+" "+str(uid[2])+" "+str(uid[3])+" "+str(uid[4])
                return (kart_uid)
                
    def result(self,sonuc):
        return sonuc
