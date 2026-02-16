from machine import Pin
import time

c1 = Pin(5, Pin.OUT)
c2 = Pin(18, Pin.OUT)
c3 = Pin(19, Pin.OUT)
c4 = Pin(22, Pin.OUT)

while True:
    c1.value(1)
    c2.value(0)
    c3.value(0)
    c4.value(0)
    time.sleep_ms(5)
    
    c1.value(0)
    c2.value(1)
    c3.value(0)
    c4.value(0)
    time.sleep_ms(5)
    
    c1.value(0)
    c2.value(0)
    c3.value(1)
    c4.value(0)
    time.sleep_ms(5)
    
    c1.value(0)
    c2.value(0)
    c3.value(0)
    c4.value(1)
    time.sleep_ms(5)
