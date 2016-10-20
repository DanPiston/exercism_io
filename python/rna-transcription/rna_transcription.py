#import argparse
#def replace(string):
#    replacements = {'a': 'b',
#                    'b': 'c',
#                    'c': 'a'}
#    new_string = list(string)
#    for index, char in enumerate(string):
#        if char in replacements:
#            new_string[index] = replacements[char]
#    return ''.join(new_string)
#def main():
#    parser = argparse.argumentparser()
#    parser.add_argument('string')
#    args = parser.parse_args()
#    new_string = replace(args.string)
#    print('old: {}'.format(args.string))
#    print('new: {}'.format(new_string))
#if __name__ == '__main__':
#    main()

def to_rna(dna):
    replacements = {'G' : 'C',
                    'C' : 'G',
                    'T' : 'A',
                    'A' : 'U'}
    new_dna = list(dna)
    for index, char in enumerate(dna):
        if char in replacements:
            new_dna[index] = replacements[char]
    return ''.join(new_dna)

print(to_rna('CGG'))
