# Example using PIO to generate a loud tone in a piezo buzzer.
import time
from machine import Pin
import rp2

FREQ = 3951    # SM clock is 14x frequency

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW,
             sideset_init=rp2.PIO.OUT_LOW)
def mod_sine():
    # generate push-pull wave in a 14-step, 5-2-5-2 pattern
    set(pins, 1) .side(0) [4]    # high - low
    set(pins, 0) .side(0) [1]    # low - low
    set(pins, 0) .side(1) [4]    # low - high
    set(pins, 0) .side(0) [1]    # low - low

# Create the StateMachine with the modified sine push-pull output on GPIO0 and GPIO1
sm = rp2.StateMachine(0, mod_sine, freq=FREQ*14, set_base=Pin(0), sideset_base=Pin(1))

# Start the StateMachine.
sm.active(1)    # start tone
time.sleep(1) 
sm.active(0)    # stop tone
