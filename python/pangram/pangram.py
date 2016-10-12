import string

def is_pangram(phrase):
    phrase = phrase.lower()
    print(phrase)
    alpha = string.ascii_lowercase
    for a in alpha:
        if a not in phrase:
            return False
        else:
            return True


print(is_pangram("ABCDEFG"))

