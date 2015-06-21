from pprint import pprint
import unittest

from markov import MarkovTextGenerator


class TestMarkov(unittest.TestCase):
    file_path = "test_file.txt"

    def test_parses_all_words(self):
        model = MarkovTextGenerator(self.file_path, 1)
        expected_words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "brown", "fox.", "Brown", "is", "a",
                          "nice", "color."]
        self.assertEqual(model.words, expected_words)

    def test_one_gram_model(self):
        model = MarkovTextGenerator(self.file_path, 1)
        word_model = model.word_model()
        expected_model = {
            ('The',): ['quick'],
            ('quick',): ['brown'],
            ('brown',): ['fox', 'fox.'],
            ('fox',): ['jumps'],
            ('fox.',): ['Brown'],
            ('the',): ['brown'],
            ('jumps',): ['over'],
            ('over',): ['the'],
            ('Brown',): ['is'],
            ('is',): ['a'],
            ('a',): ['nice'],
            ('nice',): ['color.'],
            ('color.',): []

        }
        self.assertItemsEqual(word_model.keys(), expected_model.keys())
        self.assertDictEqual(word_model, expected_model)

    def test_two_gram_model(self):
        model = MarkovTextGenerator(self.file_path, 2)
        word_model = model.word_model()
        expected_model = {
            ("The", "quick",): ["brown"],
            ("quick", "brown",): ["fox"],
            ("brown", "fox",): ["jumps"],
            ("fox", "jumps",): ["over"],
            ("jumps", "over",): ["the"],
            ("over", "the",): ["brown"],
            ("the", "brown",): ["fox."],
            ("brown", "fox.",): ["Brown"],
            ("fox.", "Brown",): ["is"],
            ("Brown", "is",): ["a"],
            ("is", "a",): ["nice"],
            ("a", "nice",): ["color."],
            ("nice", "color.",): [],

        }
        self.assertItemsEqual(word_model.keys(), expected_model.keys())
        self.assertDictEqual(word_model, expected_model)

    def test_start_words(self):
        model = MarkovTextGenerator(self.file_path, 1)
        mode2 = MarkovTextGenerator(self.file_path, 2)
        start_words_1 = model.start_words
        start_words_2 = mode2.start_words

        expected_words = ["The", "Brown"]

        self.assertItemsEqual(start_words_1, start_words_2)
        self.assertItemsEqual(expected_words, start_words_1)

    def test_start_prefixes_1(self):
        model = MarkovTextGenerator(self.file_path, 1)
        start_pairs = model.start_pairs
        expected_start_pairs = [("The",), ("Brown",)]

        self.assertItemsEqual(expected_start_pairs, start_pairs)

    def test_start_prefixes_2(self):
        model = MarkovTextGenerator(self.file_path, 2)
        start_pairs = model.start_pairs
        expected_start_pairs = [("The", "quick",), ("Brown","is",)]

        self.assertItemsEqual(expected_start_pairs, start_pairs)

    def test_simple_paragraph_one_word(self):
        model = MarkovTextGenerator(self.file_path, 1)
        sentences = model.generate(1)

        possible_sentences = model.start_words
        self.assertIn(sentences, possible_sentences)

    def test_simple_paragraph_two_words(self):
        model = MarkovTextGenerator(self.file_path, 1)
        sentences = model.generate(2)

        possible_sentences = ["The quick", "Brown is"]
        self.assertIn(sentences, possible_sentences)


    def test_model2_paragraph_two_words(self):
        model = MarkovTextGenerator(self.file_path, 2)
        sentences = model.generate(3)

        possible_sentences = ["The quick brown", "Brown is a"]
        self.assertIn(sentences, possible_sentences)