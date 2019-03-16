from __future__ import division
import time
from PCA9685ROBOT import PCA9685ROBOT

class DEVICECONTROLLER:

    @property
    def servo_controller(self):
        self._servo_controller = value

    @property
    def forward_right_motor(self, value):
        self._forward_right_motor = value
    
    @property
    def forward_left_motor(self, value):        
        self._forward_left_motor = value

    @property
    def backward_right_motor(self, value):
        self._backward_right_motor = value

    @property
    def backward_left_motor(self, value):
        self._backward_left_motor = value
    
    @property
    def update_rate(self, value):
        if(value < 1000):
            _periodic_timer_milliseconds = 1000
        elif(value > 1):
            _periodic_timer_milliseconds = 1
        else:
            _periodic_timer_milliseconds = value
                    
    @property
    def update_rate(self):
        return _periodic_timer_milliseconds


    def __init__(self, forward_right_motor, forward_left_motor, backward_right_motor, backward_left_motor):
        print('Initialize device controller')
        self._servo_controller = PCA9685ROBOT()
        self._forward_right_motor = forward_right_motor
        self._forward_left_motor = forward_left_motor
        self._backward_right_motor = backward_right_motor
        self._backward_left_motor = backward_left_motor
        self._periodic_timer_milliseconds

    

    def control_motor(self, dc_motor):
        counts = 0
        speed = dc_motor.speed_command

        # Apply speed limit
        if(speed > dc_motor.maximum_speed):
            speed = dc_motor.maximum_speed
        elif (speed < dc_motor.minimum_speed):
            speed = dc_motor.minimum_speed
        
        # Scale the speed reference to PCA9685 device 'count'
        if(dc_motor.minimum_speed == dc_motor.maximum_speed):
            counts = _servo_controller.minimum_count
        else:
            counts = int((speed - dc_motor.minimum_speed) * \
                (float(_servo_controller.maximum_count - _servo_controller.minimum_count) / (dc_motor.maximum_speed - dc_motor.minimum_speed)) \
                    + (float) _servo_controller.minimum_count)
        
        # Sart
        if(dc_motor.start_command() and not dc_motor.running_sts):
            if(dc_motor.reverse_command):
                _servo_controller.set_channel_off(dc_motor.forward_channel)
                dc_motor.forward_sts = False
                _servo_controller.set_channel_on(dc_motor.reverse_channel)
                dc_motor.reverse_sts = True
            else:
                _servo_controller.set_channel_off(dc_motor.reverse_channel)
                dc_motor.reverse_sts = False                
                _servo_controller.set_channel_on(dc_motor.forward_channel)
                dc_motor.forward_sts = True
            dc_motor.direction_last_scan = dc_motor.reverse_command
            _servo_controller.set_pwm(dc_motor.pwm_channel, _servo_controller.minimum_count, counts)
            dc_motor.count_last_scan = counts
            dc_motor.running_sts = true
        # Stop
        if(dc_motor.stop_command() and dc_motor.running_sts()):
            _servo_controller.set_channel_off(dc_motor.reverse_channel)
            _servo_controller.set_channel_off(dc_motor.forward_channel)
            _servo_controller.set_channel_off(dc_motor.pwm_channel)
            dc_motor.count_last_scan = counts
            dc_motor.running_sts = False
            dc_motor.stop_command = False

        # Speed
        if(counts != dc_motor.count_last_scan and dc_motor.running_sts):
            _servo_controller.set_pwm(dc_motor.pwm_channel, dc_motor.minimum_count, counts)
            dc_motor.count_last_scan = counts

        # Direction
        if(dc_motor.running_sts and (dc_motor.reverse_command != dc_motor.direction_last_scan)):
            if(dc_motor.reverse_command):
                _servo_controller.set_channel_off(dc_motor.forward_channel)
                dc_motor.forward_sts = False
                _servo_controller.set_channel_on(dc_motor.reverse_channel)
                dc_motor.reverse_sts = True
            else:
                _servo_controller.set_channel_off(dc_motor.reverse_channel)
                dc_motor.reverse_sts = False
                _servo_controller.set_channel_on(dc_motor.forward_channel)
                dc_motor.forward_sts = True

            dc_motor.direction_last_scan = dc_motor.reverse_command

        dc_motor.start_command = False
        dc_motor.stop_command = False

            





        



