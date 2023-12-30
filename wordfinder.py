"""Word Finder: finds random words from a dictionary."""

import random

path = "words.txt"


class WordFinder:

    """ Machine for finding random words from dictionary.
        >>> wf = WordFinder("words.txt")
        235886 words read

        >>> wf.random() in ["aardvark", "zymurgy", "aahed"]
        True

        >>> wf.random() in ["aardvark", "zymurgy", "aahed"]
        True

        >>> wf.random() in ["aardvark", "zymurgy", "aahed"]
        True
    """   


    def __init__(self, path):
        """Read dictionary and reports # items read."""
        with open(path) as dict_file:
            self.words = self.parse(dict_file)
        print(f"{len(self.words)} words read")
    
    def parse(self, dict_file):
        """Parse dict_file -> list of words."""
        return [w.strip() for w in dict_file]
    
    def random(self):
        """Return random word."""
        return random.choice(self.words)
    
wf = WordFinder(path) 

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.
        >>> swf = SpecialWordFinder("words.txt")
        235886 words read

        >>> swf.random() in ["aardvark", "zymurgy", "aahed"]
        True

        >>> swf.random() in ["aardvark", "zymurgy", "aahed"]
        True

        >>> swf.random() in ["aardvark", "zymurgy", "aahed"]
        True
    """

    def parse(self, dict_file):
        """Parse dict_file -> list of words, skipping blanks/comments."""
        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]
    
swf = SpecialWordFinder(path)

