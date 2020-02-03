from random import shuffle

import yaml
from kivy.uix.label import Label


class WordGenerator(Label):

    def __init__(self, words_path):
        super(WordGenerator, self).__init__()
        self.all_words = self.read_file(words_path)

    def read_file(self, path) -> dict:
        with open(path, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def generate_word(self, difficulty):
        print(self.all_words)
        shuffle(self.all_words[difficulty])
        return self.all_words[difficulty][-1]
