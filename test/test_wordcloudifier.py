import sys
import unittest

sys.path.append('../program/')
import wordcloudifier as wcld

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
        wc = wcld.Wordcloudifier('../program/stopwords.txt')
        wc.user_text_and_clean()
        # Need automated way of adding user input text here
        # tmpvar to hold first batch of user words
        tmp = wc.get_user_words
        assert tmp is not None
        # user words should change now
        wc.iterate()
        new = wc.get_user_words()
        assert tmp is not new

    def test_display(self):
        wc = wcld.Wordcloudifier('../program/stopwords.txt')
        wc.user_text_and_clean()
        wc.iterate()
        wc.display()

#    def test_bad_constructor(self):
#        try:
#            bad_wc = wcld.Wordcloudifier('doesntexist.txt')
#            self.fail("Didn't raise IOError")
#        except IOError, io:
#            self.assertEquals("That's not a file!", io.message)

#    def test_add_stopwords(self):
#	wc = wcld.Wordcloudifier('../program/stopwords.txt')
#	assert 'wubbalubbadubdub' in wc.get_stopwords_list()

if __name__ == '__main__':
    unittest.main()
