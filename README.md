# AutoCensor.ai

This web app allows automatic censoring of audio files using machine learning and audio processing.

# Update - Dec 11, 2019 - Prototype Phase

<h3>AutoCensor API -</h3>
<ul>
    <li>Central API that controls everything.</li>
    <li>It is the main.py that creates a Server using Flask.</li>
    <li>It is the Hub for all the Modules.</li>
</ul>

<h3>User Interface -</h3>
<ul>
    <li>It is a Web Based UI.</li>
    <li>It is the portal where all the User Interaction takes place.</li>
    <li>Index.html is used to access this portal.</li>
</ul>

<h3>Other -</h3>
<ul>
    <li>Central API controls all the other modules too.<br>
    <li>FIle System is used to access the Audio file to be processed.<br>
    <li>Google Speech-To-Text API is used by get the precise transcript of the audio.<br>
    <li>Audio Processing Module is used to process the Given Audio.<br>
</ul>

<h3>Future -</h3>
<ul>
    <li>This is Project is right now in a Prototype Phase.</li>
    <li>Try to Implement better Speech Recognition.</li>
    <li>Real Time implementation for Live Streaming.</li>
    <li>Better Editing Tools.</li>
    <li>Implement Deep Learning Model to Recognize Explicit Content.</li>
</ul>
