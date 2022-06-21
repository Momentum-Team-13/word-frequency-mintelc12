STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

import string


title = """
  _____  _      _   _                              
 |  __ \(_)    | | (_)                             
 | |  | |_  ___| |_ _  ___  _ __   __ _ _ __ _   _ 
 | |  | | |/ __| __| |/ _ \| '_ \ / _` | '__| | | |
 | |__| | | (__| |_| | (_) | | | | (_| | |  | |_| |
 |_____/|_|\___|\__|_|\___/|_| |_|\__,_|_|   \__, |
                                              __/ |
                                             |___/ 
                                            """
print(title)

def print_word_freq(file):
    """Read in `file` and print out the frequency of words in that file. Your code goes here."""
    print (f"Your file is: {file}")
    with open(file) as open_file:
        read_file = open_file.read()
    # print(read_file)

# for word in 

    poem = read_file.translate(str.maketrans("", "", string.punctuation))
    poem = poem.lower()
    words = poem.split()
    # print(poem)
    # print(words)
    for word in words.copy():
        if word in STOP_WORDS:
            words.remove(word)
    unique_words = {"song": 1}

    for word in words:
        if word not in unique_words:
            unique_words[word] = 1 
        else:
            unique_words[word] +=1
            #{word: (value + 1)}
            # print(unique_words[word])
    sort_unique_words = sorted(unique_words.items(), key=lambda x: x[1], reverse=True)
    for i in sort_unique_words[:10]:
        print(f'{i[0]:10} | {i[1]} {"*" * i[1]}')
    # print(unique_words)


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
