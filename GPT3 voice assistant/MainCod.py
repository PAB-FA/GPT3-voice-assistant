import sounddevice as sd
import numpy as np
import soundfile as sf
from pydub import AudioSegment
from POpenAI import AI , pr
from pygame import mixer
import random

mixer.init()
fs = 22050
recording = np.array([])
def callback(indata, frames, time, status):
    global recording
    recording = np.append(recording, indata)
stream = sd.InputStream(callback=callback, channels=1, samplerate=fs)
stream.start()
VE = 0
VS = 0
def SelectVoice(indata, outdata, frames, time, status):
    global recording
    global VE ,VS
    VMS = 35
    VSV = 60
    VRST = VSV + 5
    VCLR = VSV + 10
    VVS = 8
    Noize = True
    volume_norm = np.linalg.norm(indata)*10
    if int(volume_norm) > VMS :
        VE = 0
        print("Recording started")
        stream.start()  # شروع ضبط
        VS = VS + 1
        print(VS)
    if int(volume_norm) < VMS - 5 :
        VE = VE + 1
    if VE > VSV and VS > VVS:
        mixer.music.load('./File/EF/1.mp3')
        mixer.music.play()
        File = './File/TempVoice/'+'Temp' + str(random.randint(10000000000, 99999999999)) + '.wav'
        stream.stop()  # توقف ضبط
        sf.write(File, recording, fs)
        VS = 0
        recording = np.array([])  # پاک کردن آرایه ضبط قبلی
        print("Recording stopped")
        Text = AI(File=File,Mode='ST')
        pr(Text)
        if Text != 'Len < 2' :
            Text = AI(In = Text)
            mixer.music.load('./File/EF/2.mp3')
            mixer.music.play()
            file = AI(Mode = 'TS',In = Text,File=File+'.mp3')
            mixer.music.load(file)
            mixer.music.play()
            while mixer.music.get_busy():
                pass
    if VE > VRST : VS = 0
    if VE > VCLR : recording = np.array([])

with sd.Stream(callback=SelectVoice):
    sd.sleep(10000000)
