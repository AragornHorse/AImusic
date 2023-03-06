import sounddevice as sd
from scipy.io.wavfile import write
from Music import play_midi
from threading import Thread

class piano(Thread):
    def run(self):
        play_midi()

# sd.default.device[0] = 11

class saver(Thread):
    def run(self):
        fs = 16000  # Sample rate
        seconds = 5  # Duration of recording

        myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=1, )
        sd.wait()  # Wait until recording is finished

        write('output.wav', fs, myrecording)  # Save as WAV file


p = piano()
# s = saver()

# s.start()
p.start()

# print(sd.query_devices())
# print(sd.default.device[0])

