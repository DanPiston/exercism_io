def distance(strand1, strand2):
    index = 0
    distance = 0
    while index < len(strand1):
        if strand1[index] != strand2[index]:
            distance += 1
        index += 1
    return distance


