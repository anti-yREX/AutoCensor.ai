""" #  Beep Out Audio - Implemented
    #Next Tasks
    #1 Read the Audio File
    #4 Edit the Audio File
    #5 Save the Audio File

    import wave
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
"""
""" #  Convert MP3 to WAV

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
    src = "audios/audio1.mp3"
    src = convert_mp3_to_wav(src)
"""

""" #  Convert MP3  to RAW
    from os import path
    from pydub import AudioSegment

    def make_dst(src):
        i = len(src) - 1
        while(i >= 0):
            if(src[i] == '.'):
                dot = i
            i -= 1
        
        dst = ""
        
        for i in  range(0,dot):
            dst += src[i]
        dst  = dst + "_raw.raw"
        return dst

    def convert_mp3_to_raw(src):
        # files                                                                         
        dst = make_dst(src)
        print(src + "\n" + dst)
        # convert wav to mp3                                                            
        sound = AudioSegment.from_mp3(src)
        sound.export(dst, format="raw")
        return dst
    src = "audios/audio1.mp3"
    src = convert_mp3_to_raw(src)
"""

"""#  Recieve from Front End
    from flask import Flask, request, jsonify
    #from main import *
    app = Flask(__name__)

    @app.route('/api/', methods=["POST"])
    def main_interface():
        response = request.get_json()
        print(response["message"])
        response["message"]=compute(response["message"])
        return jsonify(response)

    @app.after_request
    def add_headers(response):
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
        return response
    if __name__ == '__main__':
        app.run(debug=True)  
"""