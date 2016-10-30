def word_count(word):
    words = word.split()
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts
    


print(word_count('testing 1 2 testing'))
