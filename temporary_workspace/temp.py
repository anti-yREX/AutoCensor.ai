import wave

"""
Audio 1 - 1000ms - 2100ms
"""
    
beep = "audios/unit_beep.wav"
b = wave.open(beep, 'r')
#Frame a Milisecond are different .. Calculate in Frames  1000ms = 44100 frames 
#Make a Longer Beep


print(b.getparams())
src = "audios/audio1_wav.wav"
dst = "audios/edited_audio1_wav.wav"
a = wave.open(src, 'r')
t = wave.open(dst, 'w')
t.setparams(a.getparams())
st = int(0.938 * 44100)
ed = int(2.1 * 44100)
t.writeframes(a.readframes(st))
while(t.tell() <= ed):
    b.setpos(0)
    t.writeframes(b.readframes(50))
a.setpos(ed)
t.writeframes(a.readframes(a.getnframes()-ed))
b.close()
t.close()
a.close()