#!/usr/bin/env python3

from ev3dev2.motor import MoveTank,OUTPUT_A, OUTPUT_D 
from ev3dev2.sensor.lego import UltrasonicSensor
from ev3dev2.button import Button
from time import sleep
import logging

btn = Button()
tank_pair = MoveTank(OUTPUT_A, OUTPUT_D)
 
while not btn.any():
    x=input("press arrow keys")
    if x=='f':
        tank_pair.on(left_speed = 0, right_speed = 0)
        tank_pair.on(left_speed = 50, right_speed = 50)

    elif x=='b':
        tank_pair.on(left_speed = 0, right_speed = 0)
        tank_pair.on(left_speed = -50, right_speed = -50)

    elif x=='l':
        tank_pair.on(left_speed = 0, right_speed = 0)
        tank_pair.on(left_speed = 50, right_speed = 0)

    elif x=='r':
        tank_pair.on(left_speed = 0, right_speed = 0)
        tank_pair.on(left_speed = 0, right_speed = 50)

    elif x=='s':
        tank_pair.on(left_speed = 0, right_speed = 0) 
        
    else:
         break
        

