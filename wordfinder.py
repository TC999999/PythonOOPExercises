"""Word Finder: finds random words from a dictionary."""

from random import randint


class WordFinder:
    """Creates a list of words from a file

    Attributes
    ----------------
    filename: str
        the name and path of the file of words you wish to find

    >>> wf = WordFinder("less_words.txt")
    3 words read

    >>> wf.random() in ['cat', 'dog', 'porcupine']
    True

    """

    def __init__(self, filename):
        """creates the list of words from the file and counts the number of words in the file"""
        self.filename = filename
        self.file = open(self.filename, "r")
        self.text = self.file.read()
        self.word_list = self.parse()
        self.file.close()
        print(f"{len(self.word_list)} words read")

    def parse(self):
        """parses out the newlines to make a list of words"""
        return self.text.split("\n")

    def random(self):
        """generates a random index of the word list to return"""
        index = randint(0, len(self.word_list) - 1)
        return self.word_list[index]


class SpecialWordFinder(WordFinder):
    """for special cases when a list has comments and spaces

    >>> wf2 = SpecialWordFinder("sub_words.txt")
    4 words read

    >>> wf2.random() in ['kale', 'parsnips', 'apple', 'mango']
    True

    """

    def parse(self):
        """rewrites the word list to filter out the comments and spaces"""
        words = self.text.split("\n")
        return [word for word in words if not word.startswith("#") and word != ""]
