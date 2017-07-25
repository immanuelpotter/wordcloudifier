import unittest

from program import wordcloudifier

def test_function_actually_works():
	wordcloudifier.myFunc()
	l = ('foo', 'bar', 'test','is')
	assert l[3] in stopwords_list

def test_add_stopwords():
	wordcloudifier.myFunc()
	wordcloudifier.addStopwords('wubbalubbadubdub')
	assert 'wubbalubbadubdub' in stopwords_list
