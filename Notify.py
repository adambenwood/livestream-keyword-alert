import requests

from config import config


def text_alert(context, keywords, confidence):
    report = {}
    report["value1"] = ' '.join(map(str, context))
    report["value2"] = str(keywords)
    report["value3"] = "{0:.2f}".format(confidence)
    api_key = config()['Secrets']['ifttt_api_key']
    requests.post("https://maker.ifttt.com/trigger/key_words_detected/with/key/{}".format(api_key), data=report)
