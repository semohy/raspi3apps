from random import randint


def main():
    olasilik()
    tutulanSayi()

    print("Sayı tahmin Oyunu , doğru tahmin olasılığı :%",rand*10)
    prediction = input("Tahmin Sayınızı giriniz :")

    

def olasilik():
  global  rand
  rand = randint(0,9)
  if(rand == 0):
      rand = randint(0,9)
  return rand

def tutulanSayi():
    global tutulanSayi
    tutulanSayi = randint(0,9)
    return tutulanSayi

def tahminSayisi(tahminSayi,olasilik,tutulanSayi):
    counter = 0
    while(tutulanSayi != tahminSayi):
        for (counter <= 2):
            randSayi = randint(0,9)
            counter = counter+1
    if()
            
    

while True:
    try:
        main()
    except KeyboardInterrupt: 
         interruptState = input("Çıkmak için e tuşla dvam etmek içise c")
         if(interruptState == "e"):
             exit()
         elif (interruptState == "c" ):
             main()
