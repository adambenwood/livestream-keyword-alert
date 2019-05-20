import os
from typing import List, Any

import Notify
import SpeechToText
import NLP
import multiprocessing
import time
import ffmpy

LOOPS = 2
stream_url = "http://ykf.dyndns.org:8000/wrps7.ogg"
KEYWORDS = ['marker', '279']

if __name__ == '__main__':

    for i in range(LOOPS):  # each loop is roughly going to be 1:30
        os.remove("temp.flac")
        p = multiprocessing.Process(target=SpeechToText.record_snip, name="Foo", args=(stream_url,))
        p.start()  # Start listening to scanner
        print("Recording Audio")
        # Wait 40 seconds for foo
        time.sleep(40)  # Listen for 40 seconds

        # Terminate foo
        p.terminate()  # Stop listening
        # Cleanup
        p.join()

        print("Recording Finished / Starting Second Recording Process")
        s = multiprocessing.Process(target=SpeechToText.record_snip, name="Foo2", args=(stream_url,))
        s.start()  # Start listening where first process left off

        # Convert to FLAC so Google SpeechToText can read file
        print("Converting to FLAC")
        ff = ffmpy.FFmpeg(
            inputs={'temp.ogg': None},

            outputs={'temp.flac': None}
        )
        ff.run()

        # The name of the audio file to transcribe
        file_name = os.path.join(
            os.path.dirname(__file__),
            'temp.flac')
        print("Performing SpeechToText Analysis")
        word_list, confidence = SpeechToText.speech_to_text(file_name)
        location_trigger, keywords = NLP.check_for_location(word_list, KEYWORDS)  # type: (bool, List[Any])

        if location_trigger is True:
            print("Keywords Detected: Sending Alert for Keyword(s): " + str(
                keywords) + " Confidence = " + "{0:.2f}".format(confidence))
            Notify.text_alert(word_list, keywords, confidence)

        os.remove("temp.flac")
        print("No keywords detected")
        time.sleep(35)
        s.terminate()
        s.join()

        print("Converting to FLAC")
        ff = ffmpy.FFmpeg(
            inputs={'temp.ogg': None},

            outputs={'temp.flac': None}
        )
        ff.run()

        # The name of the audio file to transcribe
        file_name = os.path.join(
            os.path.dirname(__file__),
            'temp.flac')
        print("Performing SpeechToText Analysis")
        word_list, confidence = SpeechToText.speech_to_text(file_name)
        location_trigger, keywords = NLP.check_for_location(word_list, KEYWORDS)  # type: (bool, List[Any])

        if location_trigger is True:
            print("Keywords Detected: Sending Alert for Keyword(s): " + str(
                keywords) + " Confidence = " + "{0:.2f}".format(confidence))
            Notify.text_alert(word_list, keywords, confidence)
        # need to fix this multiprocessing
        print("continuing...")
