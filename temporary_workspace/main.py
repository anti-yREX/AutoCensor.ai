"""

===> TO DO

1 -> Read the Audio File (Done)
    1.1-> If audio in .mp3 convert to .wav  (Done) (Saved in temp.py)
2 -> Run it on speech to text API
3 -> Check the Transcript for Wrong Words
4 -> Edit the Audio File (Done)
5 -> Save the File (Done)
6 -> Save the marked word into a JSON text file

"""

import wave
def make_dst(src):
    i = len(src) - 1
    while(i >= 0):
        if(src[i] == '.'):
            dot = i
        i -= 1
    
    dst = ""
    
    for i in  range(0,dot):
        dst += src[i]
    dst  = dst + "_edited.wav"
    return dst



def beep(src, strt, end):
    dst = make_dst(src)
    
    beep = "audios/unit_beep.wav"
    b = wave.open(beep, 'r')

    #1 Read the Audio File
    a = wave.open(src, 'r')
    t = wave.open(dst, 'w')
    t.setparams(a.getparams())

    #4 Edit the Audio File
    st = int(strt * 44100)
    ed = int(end * 44100)

    t.writeframes(a.readframes(st))

    while(t.tell() <= ed):
        b.setpos(0)
        t.writeframes(b.readframes(50))

    a.setpos(ed)
    t.writeframes(a.readframes(a.getnframes()-ed))

    #5 Save the Audio File
    b.close()
    t.close()
    a.close()
    return dst

src = "audios/audio1_wav.wav"
src = beep(src, 0.983, 2.1)
print(src)



#Next Tasks
