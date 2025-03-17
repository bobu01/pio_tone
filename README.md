# pio_tone
Beep and chime experiments using RP2040 PIO.

Projects can often benefit from audio feedback to the end user. PWM and timers have been used to generate beeps, tones and clicks longer than anyone can remember. Let's try to use the PIO state machine peripheral found in RP2040 MCU to generate waveforms for sounds. The PIO can work independently and be triggered by the main processor. The M0+ core of the RP2040 is fast, but generating a sound waveform can take time from the main tasks.

Target Hardware: Raspberry Pi Pico board and a small piezo buzzer.  A 100 ohm resistor is connected between the GPIO and the buzzer. This reduces electrical noise on digital pins.

Goals: Generate simple square waves, then try other waves using the PIO to generate PWM.

Nothing much here. Just starting ...
- sq_tone_demo.py:  Generate square wave tone for a piezo buzzer with a specified number of pulses. Main program puts a value to trigger the state machine. The state machine counts the cycles and stops. Frequency is 3951 Hz because that was the loudest note from this buzzer. Buzzer is wired from GPIO0 to GND with a resistor in series.
- pio_5252a.py:  A demo of a push-pull drive for a piezo buzzer. This uses a modified sine pattern in 5-2-5-2 timing. The same buzzer and resistor are connected from GPIO0 to GPIO1.This is much louder. There's no cycle counter yet. SM frequency is 14x the tone (5+2+5+2=14).
- Next compare to a square push-pull wave.
