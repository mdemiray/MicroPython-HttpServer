import socket
import machine


#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title>ESP8266 LED ON/OFF</title> </head>
<h2>Http Web Server to turn On/Off Leds Wirelessly</h2></center>
<h3>ESP8266 with MicroPython</h3></center>
<form>
LED 1&nbsp;&nbsp;:
<button name="LED" value="ON_1" type="submit">LED ON</button>
<button name="LED" value="OFF_1" type="submit">LED OFF</button><br><br>
LED 2 :
<button name="LED" value="ON_2" type="submit">LED ON</button>
<button name="LED" value="OFF_2" type="submit">LED OFF</button><br><br>
LED 3 :
<button name="LED" value="ON_3" type="submit">LED ON</button>
<button name="LED" value="OFF_3" type="submit">LED OFF</button><br><br>
LED 4 :
<button name="LED" value="ON_4" type="submit">LED ON</button>
<button name="LED" value="OFF_4" type="submit">LED OFF</button><br><br>
LED 5 :
<button name="LED" value="ON_5" type="submit">LED ON</button>
<button name="LED" value="OFF_5" type="submit">LED OFF</button><br><br>
LED 6 :
<button name="LED" value="ON_6" type="submit">LED ON</button>
<button name="LED" value="OFF_6" type="submit">LED OFF</button><br><br>
</form>
</html>
"""

#Setup PINS
LED_1 = machine.Pin(16, machine.Pin.OUT)
LED_2 = machine.Pin(5, machine.Pin.OUT)
LED_3 = machine.Pin(4, machine.Pin.OUT)
LED_4 = machine.Pin(0, machine.Pin.OUT)
LED_5 = machine.Pin(2, machine.Pin.OUT)
LED_6 = machine.Pin(14, machine.Pin.OUT)


#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:

    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    LEDON_1 = request.find('/?LED=ON_1')
    LEDOFF_1 = request.find('/?LED=OFF_1')
    LEDON_2 = request.find('/?LED=ON_2')
    LEDOFF_2 = request.find('/?LED=OFF_2')
    LEDON_3 = request.find('/?LED=ON_3')
    LEDOFF_3 = request.find('/?LED=OFF_3')    
    LEDON_4 = request.find('/?LED=ON_4')
    LEDOFF_4 = request.find('/?LED=OFF_4')
    LEDON_5 = request.find('/?LED=ON_5')
    LEDOFF_5 = request.find('/?LED=OFF_5')      
    LEDON_6 = request.find('/?LED=ON_6')
    LEDOFF_6 = request.find('/?LED=OFF_6')   

    if LEDON_1 == 6:
        print('TURN LED0 ON')
        LED_1.on()
    if LEDOFF_1 == 6:
        print('TURN LED0 OFF')
        LED_1.off()
    if LEDON_2 == 6:
        print('TURN LED2 ON')
        LED_2.on()
    if LEDOFF_2 == 6:
        print('TURN LED2 OFF')
        LED_2.off()
    if LEDON_3 == 6:
        print('TURN LED2 ON')
        LED_3.on()
    if LEDOFF_3 == 6:
        print('TURN LED2 OFF')
        LED_3.off()
    if LEDON_4 == 6:
        print('TURN LED2 ON')
        LED_4.on()
    if LEDOFF_4 == 6:
        print('TURN LED2 OFF')
        LED_4.off()  
    if LEDON_5 == 6:
        print('TURN LED2 ON')
        LED_5.on()
    if LEDOFF_5 == 6:
        print('TURN LED2 OFF')
        LED_5.off()
    if LEDON_6 == 6:
        print('TURN LED2 ON')
        LED_6.on()
    if LEDOFF_6 == 6:
        print('TURN LED2 OFF')
        LED_6.off()    
    response = html
    conn.send(response)
    conn.close()
