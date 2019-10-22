#!/usr/bin/env python 3.6

"""
The collocations script includes some functions to preprocess 
collocations.
"""

from nltk.collocations import BigramCollocationFinder as biCollocations
from nltk.metrics import BigramAssocMeasures

class CollocationList:
	def __init__ (self,text):
		self.text = text
		self.words = []
		print(type(self.text),'***************')
		if isinstance(self.text,str):
			self.words = self.text.split()
		elif isinstance(self.text,list):
			for file in self.text:
				with open(file) as doc:
					self.words.extend(doc.read().split())
		
		self.score_fn = BigramAssocMeasures.likelihood_ratio

	def find_collocations(self):
		"""Find collocations based on NLTK"""
		self.collocations_list = biCollocations.from_words(self.words)

	def write(self, path :str):
		"""Write the list of collocations tuples in a txt."""
		with open(path) as doc:
			for element in self.collocations_list:
				doc.write(str(element)+'\n')
	
	def head(self, N :int):
		"""Show the first N elements of the collocation list based
		on the score function "likelihood_ratio.
		"""
		return [p for p, s in self.collocations_list.score_ngrams(self.score_fn)[:N]]

	def tail(self, N :int):
		"""Show the last N elements of the collocation list based
		on the score function "likelihood_ratio."""
		return [p for p, s in self.collocations_list.score_ngrams(self.score_fn)[-N:]]

