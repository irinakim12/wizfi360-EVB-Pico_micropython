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

'''
Print WIZFI360 AT comand version and SDK details
'''
wizfi360_at_ver = wizfi01.getVersion()
if(wizfi360_at_ver != None):
    print(wizfi360_at_ver)

'''
set the current WiFi in SoftAP+STA
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
print("Now it's time to start HTTP Get/Post Operation.......\r\n")

while(1):    
    led.toggle()
    time.sleep(1)
    
    '''
    Going to do HTTP Get Operation with www.httpbin.org/ip, It return the IP address of the connected device
    '''
    #httpCode, httpRes = wizfi01.doHttpGet("www.httpbin.org","/ip","RaspberryPi-Pico", port=80)
    #httpCode, httpRes = wizfi01.doHttpGet("www.kma.go.kr","/wid/queryDFSRSS.jsp?zone=4113554500", None,port=80)
    httpCode, httpRes = wizfi01.doHttpGet("www.httpbin.org","/get",None, port=80)
    #print("------------- www.httpbin.org/ip Get Operation Result -----------------------")
    print("HTTP Code:",httpCode)
    print("HTTP Response:",httpRes)
    print("-----------------------------------------------------------------------------\r\n\r\n")
    
    
    '''
    Going to do HTTP Post Operation with www.httpbin.org/post
    '''
    post_json="{\"name\":\"Noyel\"}"
    #httpCode, httpRes = wizfi01.doHttpPost("www.httpbin.org", "application/json",post_json,"/post",None,port=80)
    httpCode, httpRes = wizfi01.doHttpPost("www.httpbin.org", "/post",post_json,"/post","RPi-Pico",port=80)
    print("------------- www.httpbin.org/post Post Operation Result -----------------------")
    print("HTTP Code:",httpCode)
    print("HTTP Response:",httpRes)
    print("--------------------------------------------------------------------------------\r\n\r\n")
    #break