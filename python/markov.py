#!/usr/bin/env python
from random import choice
import logging
import argparse
import sys

logging.basicConfig(filename='markov.log', filemode='w', level=logging.DEBUG)
console_handler = logging.StreamHandler(sys.stdout)
console_handler.setLevel(logging.INFO)
logging.getLogger().addHandler(console_handler)

class MarkovTextGenerator(object):
    """
    :type file_path : string
    :type gram_length : int
    :type words : list[str]
    :type model : dict[tuple,str ]
    :type start_pairs : list[tuple]
    :type start_words : set
    """

    def __init__(self, file_path, gram_length):
        self.gram_length = gram_length
        self.words = []
        self.model = {}
        self.start_words = set()
        self.start_pairs = []

        self.__parse_words_in_file(file_path)
        self.__build_word_model()

    def __parse_words_in_file(self, file_path):
        """
        Parses the words in the file
        :type file_path : str
        :return:
        """
        with open(file_path) as f:
            for line in f:
                for index, word in enumerate(line.split()):
                    word = word.strip()
                    if len(word)>0:
                        self.words.append(word)
                        if index == 0:  # first word
                            # add to list of start words
                            self.start_words.add(word)

    def words_in_file(self):
        """
        Returns the words parsed from the file
        :return: list[str]
        """
        return self.words

    def __build_word_model(self):
        """
        Builds the n-gram model
        :return:
        """

        for i in range(len(self.words)):
            try:
                key = tuple(self.words[i:i + self.gram_length])
                if self.words[i] in self.start_words:  # word is a start word
                    self.start_pairs.append(key)  # add to set of start keys
                if key not in self.model:
                    self.model[key] = []
                self.model[key].append(self.words[i + self.gram_length])
            except IndexError:
                break

    def word_model(self):
        """
        Returns the build n_gram model
        :return:dict[tuple,str ]
        """
        return self.model

    def generate(self, word_length):
        paragraph = []

        # for the first time choose a word from the start list
        prefix = self.__rand_start_prefix()
        logging.debug("Starting  prefix is %s" % (','.join(prefix)))

        while (len(paragraph) < word_length):
            word = prefix[0]
            paragraph.append(word)

            suffix_choices = self.model[prefix]

            if len(suffix_choices) == 0:
                logging.warn('prefix %s has no suffix choices. Will choose random start prefix' % (','.join(prefix)))
                prefix = self.__rand_start_prefix()
            else:
                suffix_choice = choice(suffix_choices)
                prefix = self.__update_key(prefix, suffix_choice)
            logging.debug("New  prefix is %s" % (','.join(prefix)))

        combined_words = " ".join(paragraph)
        return combined_words

    def __rand_start_prefix(self):
        """
        Return a random start prefix
        :return: tuple
        """
        return choice(self.start_pairs)

    def __update_key(self, tuple_elem, new_elem):
        """
        Takes a tuple. Removes the first elem and adds the new elem to the
        end of the list
        :param tuple_elem: tuple
        :param new_elem: str
        :return: tuple
        """
        tuple_as_list = list(tuple_elem)
        other_elems = tuple_as_list[1:]
        if len(other_elems) == 0:
            final_tuple = (new_elem,)
        else:
            other_elems.append(new_elem)
            final_tuple = tuple(other_elems)
        return final_tuple


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Markov Text generator.')
    parser.add_argument('file_path', type=str, help='path of the file to use to build the model')
    parser.add_argument('word_length', type=int, help='number of words to generate')
    parser.add_argument("-n", "--ngram", type=int, help="prefix length, default is 2", default=2)

    args = parser.parse_args()

    file_path = args.file_path
    word_length = args.word_length
    ngram = args.ngram

    logging.debug("Going to generate model from file %s with prefix length %s" % (file_path, ngram))
    logging.debug("Will generate %s words " % (word_length))

    markov = MarkovTextGenerator(file_path, gram_length=ngram)
    senteces = markov.generate(word_length)

    logging.info("Generated sentences:")
    logging.info(senteces)
