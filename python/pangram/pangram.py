import string

def is_pangram(phrase):
    phrase = phrase.lower()
    abc = set(string.ascii_lowercase)
    for a in abc:
        if not a in phrase:
            return False
    return True
