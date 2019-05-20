import requests


def text_alert(context, keywords, confidence):
    report = {}
    report["value1"] = ' '.join(map(str, context))
    report["value2"] = str(keywords)
    report["value3"] = "{0:.2f}".format(confidence)
    requests.post("https://maker.ifttt.com/trigger/key_words_detected/with/key/bdZgJ35uKemnRzd3uJUfDe", data=report)
