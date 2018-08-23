import sys
sys.path.append('../program/')

import wordcloudifier as wcld
import unittest
import __builtin__
from contextlib import contextmanager

@contextmanager
def mockRawInput(mock):
    original_raw_input = __builtin__.raw_input
    __builtin__.raw_input = lambda _: mock
    yield
    __builtin__.raw_input = original_raw_input

class TestWordcloudifierMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_constructor(self):
        wc = wcld.Wordcloudifier('../program/stopwords.txt')
        arr = ('foo', 'bar','very','can','will', 'test','is')

        assert arr[0] not in wc.get_stopwords_list()
        assert arr[1] not in wc.get_stopwords_list()
        assert arr[2] in wc.get_stopwords_list()
        assert arr[3] in wc.get_stopwords_list()
        assert arr[4] in wc.get_stopwords_list()
        assert arr[5] not in wc.get_stopwords_list()
        assert arr[6] in wc.get_stopwords_list()
        self.assertIsNone(wc.get_user_words())

    def test_user_input(self):
        with mockRawInput('test test 123 one two two case testcase'):
            wc = wcld.Wordcloudifier('../program/stopwords.txt')
            wc.user_text_and_clean()
            # tmpvar to hold first batch of user words
            tmp = wc.get_user_words
            assert tmp is not None
            # user words should change now
            wc.iterate()
            new = wc.get_user_words()
            assert tmp is not new

    def test_display(self):
        with mockRawInput('test test 123 one two two case testcase'):
            wc = wcld.Wordcloudifier('../program/stopwords.txt')
            wc.user_text_and_clean()
            wc.iterate()
            # Need automated way of closing/exiting app
            wc.display()


#    def test_add_stopwords(self):
#	wc = wcld.Wordcloudifier('../program/stopwords.txt')
#	assert 'wubbalubbadubdub' in wc.get_stopwords_list()

if __name__ == "__main__":
    unittest.main()
