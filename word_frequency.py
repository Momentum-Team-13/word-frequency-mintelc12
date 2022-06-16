STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

import string

#def print_word_freq(file):
"""Read in `file` and print out the frequency of words in that file. Your code goes here."""
    #print (f"Your file is: {file}")
    #with open(file) as open_file:
        #read_file = open_file.read()
    #print(read_file)
test_sentence = "How long, how long must we sing this song? How long?"

new_string = test_sentence.translate(str.maketrans("", "", string.punctuation))
print(test_sentence.lower())


new_string = new_string.lower()
words = new_string.split()
unique = {"song": 1}
# value = 1
for word in words:
    if word not in unique:
        unique.update({word: 1}) 
    else:
        unique[word]
        #{word: (value + 1)}
        print(unique[word])


    #new_string = new_string.split()
    #for word in new_string:
        #if word in STOP_WORDS:
            #new_string = list(filter((word).__ne__, new_string))
    #print(new_string)

#print_word_freq("praise_song_for_the_day.txt")







#python program that allows you to run from the command line and pass the name of the file

# if __name__ == "__main__":
#     import argparse
#     from pathlib import Path

#     parser = argparse.ArgumentParser(
#         description='Get the word frequency in a text file.')
#     parser.add_argument('file', help='file to read')
#     args = parser.parse_args()

#     file = Path(args.file)
#     if file.is_file():
#         print_word_freq(file)
#     else:
#         print(f"{file} does not exist!")
#         exit(1)
