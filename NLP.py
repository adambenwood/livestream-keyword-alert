import string
CODES = ['930', '961', '963', '974', '973', '222']


def check_for_location(word_list, KEYWORDS):
    keywords = []
    for word in word_list:
        translator = str.maketrans('', '', string.punctuation)
        word.translate(translator)
        word.lower()
        if any(word in KEYWORDS):
            keywords.append(word)
        if any(word in CODES):
            keywords.append(word)
    if len(keywords) != 0:
        return True, keywords
    else:
        return False, keywords

