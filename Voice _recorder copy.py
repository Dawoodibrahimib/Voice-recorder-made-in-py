import sounddevice
from scipy.io.wavfile import write

import time
fs = 44100
second = int (input ("Enter duration of Seconds:"))
time.sleep(1)
print ("Recording.....")
record_voice = sounddevice.rec( int (second * fs),samplerate = fs,channels = 2)
sounddevice.wait()
write("out.wav",fs,record_voice)
time.sleep(1)
print("Finished...\nPlease Check it...")

