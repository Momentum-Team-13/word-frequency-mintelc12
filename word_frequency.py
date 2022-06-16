STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

import string

def print_word_freq(file):
    """Read in 'file' and print out the frequency of words in that file. YOUR CODE GOES HERE"""
    # print (f'Your file is: {file}')
    with open(file) as open_file:
        read_file = open_file.read()
    print(read_file)

    new_string = read_file.translate(str.maketrans("", "", string.punctuation))
    print(new_string.lower())

print_word_freq("praise_song_for_the_day.txt")





#Testing import string below:

#a_string = '!hi. wh?at is the weat[h]er lik?e.'
#new_string = a_string.translate(str.maketrans('', '', string.punctuation))
#print(new_string)

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file. Your code goes here."""
    print (f"Your file is: {file}")
    with open(file) as open_file:
        read_file = open_file.read()
    print(read_file)

#python program that allows you to run from the command line and pass the name of the file

if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get the word frequency in a text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
