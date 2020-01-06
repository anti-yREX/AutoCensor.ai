# AutoCensor.ai

This web app allows automatic censoring of audio files using machine learning and audio processing.

# Update - Dec 11, 2019 - Prototype Phase

AutoCensor API -
    -> Central API that controls everything.
    -> It is the main.py that creates a Server using Flask.
    -> It is the Hub for all the Modules.

User Interface -
    -> It is a Web Based UI.
    -> It is the portal where all the User Interaction takes place.
    -> Index.html is used to access this portal.

Other -
    -> Central API controls all the other modules too.
    -> FIle System is used to access the Audio file to be processed.
    -> Google Speech-To-Text API is used by get the precise transcript of the audio.
    -> Audio Processing Module is used to process the Given Audio.

Future -
    -> This is Project is right now in a Prototype Phase.
    -> Try to Implement better Speech Recognition.
    -> Real Time implementation for Live Streaming.
    -> Better Editing Tools.
    -> Implement Deep Learning Model to Recognize Explicit Content.
