import urllib.request
# Imports the Google Cloud client library
from google.cloud import speech


def record_snip(stream_url):
    urllib.request.urlretrieve(stream_url, "temp.ogg")


def speech_to_text(file_name):
    word_list = []
    confidence = 0.00
    client = speech.SpeechClient()
    with open(file_name, 'rb') as audio_file:
        content = audio_file.read()

    audio = speech.types.RecognitionAudio(content=content)

    config = speech.types.RecognitionConfig(
        encoding=speech.enums.RecognitionConfig.AudioEncoding.FLAC,
        sample_rate_hertz=12000,
        language_code='en-US',
        enable_automatic_punctuation=False,
        enable_word_time_offsets=True,
        model='phone_call')

    response = client.recognize(config, audio)

    for result in response.results:
        alternative = result.alternatives[0]
        confidence = result.alternatives[0].confidence
        for word_info in alternative.words:
            word = word_info.word
            word_list.append(word)

    return word_list, confidence
