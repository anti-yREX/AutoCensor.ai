def speech_recognition(file_name):
  import io
  import os
  from google.cloud import speech
  from google.cloud.speech import enums
  from google.cloud.speech import types

  client = speech.SpeechClient()

  with io.open(file_name, 'rb') as audio_file:
      content = audio_file.read()
      audio = types.RecognitionAudio(content=content)

  config = types.RecognitionConfig(
      encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
      sample_rate_hertz=44100,
      language_code='en-US',
      enable_word_time_offsets=True)

  response = client.recognize(config, audio)
  return response

""" #  Speech Recognition - No Time Offset
  import speech_recognition as sr

  AUDIO_FILE = ("audios/audio_wav.wav") 

  r = sr.Recognizer()

  with sr.AudioFile(AUDIO_FILE) as source:
      audio = r.record(source)

  arr = r.recognize_google(audio,show_all=True)

  try:
      print("Audio Contents:\n" + str(arr))

  except sr.UnknownValueError:
      print("Google Speech Cannotbe recognised")

  except sr.RequestError as e:
      print("Could not request results from Google Speech RecognitionServive; {0}".format(e))
"""