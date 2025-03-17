# Example using PIO to generate a tone in a piezo buzzer.
import time
from machine import Pin
import rp2

FREQ = 3951    # SM clock is 4x frequency

@rp2.asm_pio(set_init=rp2.PIO.OUT_LOW)
def sq_tone():
# count cycles in a square wave loop.
    pull(block)    # wait for a value
    mov(x, osr)
    jmp(x_dec, "looplabel")   # pre-decrement
    label("looplabel")  
    set(pins, 1)  [1]
    set(pins, 0)
    jmp(x_dec, "looplabel")

# Create the StateMachine with the sq_tone program, output on GPIO0
sm = rp2.StateMachine(0, sq_tone, freq=FREQ*4, set_base=Pin(0))

# Start the StateMachine.
sm.active(1)

sm.put(100)        # trigger PIO for 100 cycles
time.sleep(0.1)    # delay time is independent of burst width
sm.put(30)
time.sleep(0.1)
sm.put(10)
time.sleep(0.1)
sm.put(5)
time.sleep(0.1)
