# pio_tone
Beep and chime experiments using RP2040 PIO.

Projects can often benefit from audio feedback to the end user. PWM and timers have been used to generate beeps, tones and clicks longer than anyone can remember. Let's try to use the PIO state machine peripheral found in RP2040 MCU to generate waveforms for sounds. The PIO can work independently and be triggered by the main processor. The M0+ core of the RP2040 is fast, but generating a sound waveform can take time from the main tasks.

Target Hardware: Raspberry Pi Pico board and a small piezo buzzer.

Goals: Generate simple square waves, then try other using the PIO to generate PWM.

Nothing much here. Just starting ...
