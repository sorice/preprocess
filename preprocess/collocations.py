#!/usr/bin/env python 3.6

"""
The collocations script includes some functions to preprocess 
collocations.
"""

from nltk.collocations import BigramCollocationFinder, TrigramCollocationFinder,\
								QuadgramCollocationFinder
from nltk.metrics import BigramAssocMeasures, TrigramAssocMeasures,\
							QuadgramAssocMeasures

from preprocess.shallow import remove_stopwords

class CollocationList:
	""""Collocations class

	It is strongly recommended that the 'text' must be preprocessed
	before start class collocations.

	:param text: The text or list of text names to be processed.
	:param ngrams: Number of grams your collocation must have [2,3,4]. 
	:param stopwords: Preprocess texts with/without stop words.
	:param lang: Language of the texts.
	:type text: str
	:type ngrams: int
	:type stopwords: bool
	:type lang: str
	:rtype: list

	:Example of use:

	from preprocess.demo import preProcessFlow
	txt = preProcessFlow(open(some.txt)).lower()
	object = CollocationList(txt)
	object.find_collocations()

	The results of collocation list is more understandable after ejecute 
	all the preprocessing pipeline.
	
	This class internaly use the function remove_stopwords.
	"""
	def __init__ (self,text, ngrams=2, stopwords=True, lang='en'):
		self.text = text
		self.words = []
		self.ngrams = ngrams
		self.lang = lang

		self.granms = {
			2: BigramCollocationFinder,
			3: TrigramCollocationFinder,
			4: QuadgramCollocationFinder
		}

		self.measures = {
			2: BigramAssocMeasures,
			3: TrigramAssocMeasures,
			4: QuadgramAssocMeasures
		}
		
		if isinstance(self.text,str):
			if stopwords:
				print("Removing stop words active, \
					run CollocationList(txt,stopwords=False)\
					to change behavior.")
				self.words = remove_stopwords(self.text, lang=self.lang).split()
			else:
				self.words = self.text.split()
		elif isinstance(self.text,list):
			for file in self.text:
				with open(file) as doc:
					if stopwords:
						print("Removing stop words active, \
							run CollocationList(txt,stopwords=False)\
							to change behavior.")
						self.words.extend(remove_stopwords(doc.read(), lang=self.lang).split())
					else:
						self.words.extend(doc.read().split())
		
		self.score_fn = self.measures[ngrams].likelihood_ratio

	#TODO: apply from toolz.curried import compose
	#find_collocations = compose(collocations(),remove_stopwords())
	#Delete the problem to handle to many if/else and manipulate parameters of both

	def find_collocations(self):
		"""Find collocations based on NLTK
		"""
		self.collocations_list = self.granms[self.ngrams].from_words(self.words)

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

