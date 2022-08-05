from machine import UART, Pin
from wizfi360 import WIZFI360
import time, sys

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("RPi-Pico MicroPython Ver:", sys.version)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


## Create On-board Led object
led=Pin(25,Pin.OUT)

## Create an WIZFI360 Object
wizfi01 = WIZFI360(1,115200,4,5)
wizfi360_at_ver = None
send_data = "Hello, WIZFI360."
Dest_IP = "192.168.50.203"

wizfi01.reStart()
'''
Print WIZFI360 AT comand version and SDK details
'''
wizfi360_at_ver = wizfi01.getVersion()
if(wizfi360_at_ver != None):
    print(wizfi360_at_ver)

'''
set the current WiFi in STA
'''
print(wizfi01.setCurrentWiFiMode(1))

#apList = wizfi01.getAvailableAPs()
#for items in apList:
#    print(items)
    #for item in tuple(items):
    #    print(item)
  
print("\r\n\r\n")

'''
Connect with the WiFi
'''
print("Try to connect with the WiFi..")
while (1):
    if "WIFI CONNECTED" in wizfi01.connectWiFi("rena","wiznet00"):
        print("WIZFI360 connect with the WiFi..")
        break;
    else:
        print(".")
        time.sleep(2)


print("\r\n\r\n")
print("Now it's time to start TCP Operation.......\r\n")

while(1):    
    led.toggle()
    time.sleep(1)
    
    '''
    Going to do TCP Client Operation 
    '''
    if (wizfi01._createTCP_UDPConnection("UDP",Dest_IP,5000,None)==True):
        ret = wizfi01.doSendData(send_data)
        
        print("------------- TCP Send -----------------------")
        print("Send_Data:",ret)
        print("-----------------------------------------------\r\n\r\n")
    else:
        print("Not Connected")
  
  

