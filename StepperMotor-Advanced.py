from machine import Pin
import time

c1 = Pin(5, Pin.OUT)
c2 = Pin(18, Pin.OUT)
c3 = Pin(19, Pin.OUT)
c4 = Pin(22, Pin.OUT)

list = [[1, 0, 0, 0],[0, 1, 0, 0],[0, 0, 1, 0],[0, 0, 0, 1]]

while True:
    for step in list:
        c1.value(step[0])
        c2.value(step[1])
        c3.value(step[2])
        c4.value(step[3])
        time.sleep_ms(5)
