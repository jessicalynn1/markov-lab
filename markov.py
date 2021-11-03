"""Generate Markov text from text files."""

from random import choice


def open_and_read_file(file_path):
    """Take file path as string; return text as string.

    Takes a string that is a file path, opens the file, and turns
    the file's contents as one string of text.
    """

    # your code goes here
    file_path = open('green-eggs.txt').read()

    return file_path

#open_and_read_file('green-eggs.txt')


def make_chains(text_string):
    """Take input text as string; return dictionary of Markov chains.

    A chain will be a key that consists of a tuple of (word1, word2)
    and the value would be a list of the word(s) that follow those two
    words in the input text.

    For example:

        >>> chains = make_chains('hi there mary hi there juanita')

    Each bigram (except the last) will be a key in chains:

        >>> sorted(chains.keys())
        [('hi', 'there'), ('mary', 'hi'), ('there', 'mary')]

    Each item in chains is a list of all possible following words:

        >>> chains[('hi', 'there')]
        ['mary', 'juanita']

        >>> chains[('there','juanita')]
        [None]
    """

    chains = {}

    # your code goes here
    text_string = open_and_read_file('green-eggs.txt')
    words = text_string.split()
    

    for i in range(len(words) - 2):
        
        chains_keys = (words[i], words[i + 1])
        # look at the dictionary key
        # and look at the word next to the last word from our current key
        # if the word is not a part of our key, append it to the list
        # for words in chains_keys:  
        if chains_keys not in chains:
            chains[chains_keys] = [words[i + 2]]
    # if the dictionary key already exists, do not overwrite the list
        else: 
            chains[chains_keys].append(words[i + 2])
      
    return chains

make_chains('green-eggs.txt')

def make_text(chains):
    """Return text from chains."""
    words = []

    # your code goes here
    dic = make_chains('green-eggs.txt')
    our_choices = str(dic.values())
    words.append(choice(our_choices))
    print(type(words[0]))
    return ' '.join(words)

make_text('green-eggs.txt')

input_path = 'green-eggs.txt'

# Open the file and turn it into one long string
input_text = open_and_read_file(input_path)

# Get a Markov chain
chains = make_chains(input_text)

# Produce random text
random_text = make_text(chains)

print(random_text)
