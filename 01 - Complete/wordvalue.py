from data import DICTIONARY, LETTER_SCORES
import pytest


def load_words():
    """Loads Dictionary into List"""
    return open(DICTIONARY,'r').read().split('\n')


def calc_word_value(word):
    """Returns the Scrabble value of any string
    str => int"""
    value = 0
    for letter in list(word):
        try:
            value += LETTER_SCORES[letter.upper()]
        except(KeyError):
            pass
    return value


def max_word_value(word_list=[]):
    max_word = ["",0]
    if not word_list:
        word_list = load_words()

    for word in word_list:
        value = calc_word_value(word)
        if value > max_word[1]:
            max_word = [word, value]
    return max_word[0]


class test(object):

    def test_load_words(self):
        assert type(load_words()) == list

    def test_calc_word_value(self):
        assert calc_word_value("Green") == 6
        assert calc_word_value("zebra") == 16

    def test_max_word_value(self):
        assert max_word_value() == 'benzalphenylhydrazone'


print(max_word_value(load_words()))
