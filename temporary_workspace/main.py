"""

===> TO DO

1 -> Read the Audio File
    1.1-> If audio in .mp3 convert to .wav  (Done)
2 -> Run it on speech to text API
3 -> Save Transcript as a JSON text file
4 -> Edit the Audio File
5 -> Save the File
6 -> Send the Path to the Web App

"""
from os import path
from pydub import AudioSegment

def convert_mp3_to_wav(src):
    # files                                                                         
    dst = make_dst(src)
    print(src + "\n" + dst)
    # convert wav to mp3                                                            
    sound = AudioSegment.from_mp3(src)
    sound.export(dst, format="wav")
    return dst

def make_dst(src):
    i = len(src) - 1
    while(i >= 0):
        if(src[i] == '.'):
            dot = i
        i -= 1
    
    dst = ""
    
    for i in  range(0,dot):
        dst += src[i]
    dst  = dst + "_wav.wav"
    return dst

src = "audios/audio1.mp3"
src = convert_mp3_to_wav(src)



"""
Audio 1 - 700  : 2000
Audio 2 - 3000 : end
"""

#Next Tasks
#1 Read the Audio File
#4 Edit the Audio File
#5 Save the Audio File

