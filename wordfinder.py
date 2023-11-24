
import random

class WordFinder:
    def __init__(self, filepath):
        """
        Initialize a WordFinder object.

        Args:
            filepath (str): The path to the file containing words.

        Attributes:
            words (list): A list to store the words read from the file.
            word_count (int): The count of words read from the file.
        """
        self.words = []
        self.word_count = 0  # Initialize word count to 0
        with open(filepath, 'r') as file:
            for line in file:
                word = line.strip()
                if word:
                    self.words.append(word)
                    self.word_count += 1  # Increment word count
        print(f'Added {self.word_count} words to the list')

    def pick_random(self):
        """Return a random word from the list of words

        >>> word_finder = WordFinder('words.txt')

        """
        random_word = random.choice(self.words)
        return random_word

class SpecialWordFinder(WordFinder):
    def __init__(self, filepath):
        """
        Initialize a SpecialWordFinder object.

        Args:
            filepath (str): The path to the file containing words.

        Attributes:
            words (list): A list to store the words read from the file (ignoring blank lines and lines starting with "#").
            word_count (int): The count of words read from the file (ignoring blank lines and lines starting with "#").
        """
        self.words = []
        self.word_count = 0  # Initialize word count to 0
        with open(filepath, 'r') as file:
            for line in file:
                line = line.strip()
                if line and not line.startswith("#"):
                    self.words.append(line)
                    self.word_count += 1  # Increment word count
        print(f'Added {self.word_count} words to the list')


word_finder = WordFinder('words.txt')

words = word_finder.words

