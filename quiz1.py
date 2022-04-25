""""data={"A":".-","B":"-...","C":"-.-","D":"-..",
      "E":".","F":"..-.","G":"--.", "H":"....",
      "I":"..","J":".---",
      "K":"-.-","L":".-..","M":"--","N":"-.",
      "O":"---","p":".--.","Q":"--.-","R":".-.",
      "S":"...","T":"-","U":"..-","V":"...-",
      "W":".--","X":"-..-","Y":"-.--","Z":"--..","0":"-----","1":".----","2":"..---","3":"...--"
     ,"4":"....-","5":".....","6":"-....","7":"--...","8":"---..","9":"----."}
text=input("enter your sentence:")
code=""
for i in text:
    if i!="":
        code=code+data[i]+""
    else:
        code=code+""
    print(code)    

print("Enter the text please...")
text=input()
text=text.upper()"""""""""



"""""""""""""""""
def found (char):
    list=[".",",","?","!",":","A","B","C","D","E","F","G","H","I","J","K"
    ,"L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"," "]
    place=(list.index(char))
    if (0<= int(place) <=4) :
        print("1",place)
    elif(5<= int(place) <=7):
        print("2",place-4)
    elif(8<= int(place) <=10):
        print("3",place-7)
    elif(11<= int(place) <=13):
        print("4",place-10)    
    elif(14<= int(place) <=16):
        print("5",place-13)
    elif(17<= int(place) <=19):
        print("6",place-16)
    elif(20<= int(place) <=23):
        print("7",place-19)
    elif(24<= int(place) <=26):
        print("8",place-23)
    elif(27<= int(place) <=30):
        print("9",place-27)
    else:
        print("0",1)


for i in range (0,len(text)):
    found(text[i])
    """""""""""""""""""""""



"""""    
def tabdile_adad(num):
 
    
    l = len(num)
 
   
    if (l == 0):
        print("reshte khali")
        return
 
    if (l > 4):
        print("tola bishtar az 4 nabashad")
        return
    yekan = ["seftr", "yek", "do", "seh",
                     "cehar", "panj", "shesh", "haft",
                     "hasht", "noh"]
    beine_10_20 = ["dah", "yazdah", "davazdah", "sizdah",
                  "chardah", "panzdah", "shanzdah",
                  "hifdah", "hejdah", "nozdah",
                  ]
    dahgan = ["", "", "bist", "si", "chel",
                     "panjah", "shast", "haftad", "hashtad",
                     "navad"]

 
    sadgan = ["sad"]
 
    print(num, ":", end=" ")
 
    if (l == 1):
        print(yekan[ord(num[0]) - 48])
        return
 
    x = 0
    while (x < len(num)):
 
        if (l >= 3):
            if (ord(num[x]) - 48 != 0):
                print(yekan[ord(num[x]) - 48],
                      end=" ")
                print(beine_10_20 [l - 3], end=" ")
 
            l -= 1
        else:
 
            if (ord(num[x]) - 48 == 1):
                sum = (ord(num[x]) - 48 +
                       ord(num[x+1]) - 48)
                print(dahgan[sum])
                return

            elif (ord(num[x]) - 48 == 2 and
                  ord(num[x + 1]) - 48 == 0):
                print("bist")
                return
 
            else:
                i = ord(num[x]) - 48
                if(i > 0):
                    print(dahgan[i], end=" ")
                else:
                    print("", end="")
                x += 1
                if(ord(num[x]) - 48 != 0):
                    print(yekan[ord(num[x]) - 48])
        x += 1
 
 

tabdile_adad("9923")
tabdile_adad("523")
tabdile_adad("89") 
tabdile_adad("8")"""""""" 

"""""""""""""""""""
 import math
def isPrime(n):
    if(n % 2 == 0 or n % 3 == 0 or n %5==0):
        return False
     
    for i in range(5,int(math.sqrt(n) + 1), 6):
        if(n % i == 0 or n % (i + 2) == 0):
            return False
     
    return True
 
def nextPrime(N):
    if (N <= 1):
        return 2
 
    prime = N
    found = False
 
    while(not found):
        prime = prime + 1
 
        if(isPrime(prime) == True):
            found = True
 
    return prime
N =int(input("adad ra vared konid:"))
print(nextPrime(N))""""""""""""""""""""""""""""""""""