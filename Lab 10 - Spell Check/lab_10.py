import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?', line)

def main():
    dictionary_file = open("dictionary.txt")

    dictionary_list = []

    for line in dictionary_file:

        line = line.strip()

        dictionary_list.append(line)

    dictionary_file.close()

    print("--- Linear Search ---")

    alice_file = open("AliceInWonderLand200.txt")

    for line in alice_file:

        word_list = split_line(line)

    for line in word_list:
        for word in word_list:


main()


