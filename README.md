# livestream-keyword-alert
Given a web stream, utilizes Google Speech-Text API to generate a real-time script to compare to given keywords and sends an alert via text or email through IFTTT if a keyword is spoken on the web stream

Utilizes ffmpy wrapper for FFMPEG (https://pypi.org/project/ffmpy/) to convert from .ogg stream to .FLAC so text-to-speech can accept input
