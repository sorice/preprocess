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

class Collocations:
	""""Collocations is a kind of grams. They are a pair or group of
	words that are habitually juxtaposed. E.g. 'strong coffee', 
	'black night'.

	This class contain more methods inside to return the most important
	tokens based on different metrics. 

	Parameters
	----------

	text: str
		  The text or list of text names to be processed.
	ngrams: int
		    Number of grams your collocation must have [2,3,4]. 
	stopwords: bool
			   Preprocess texts with/without stop words.
	lang: str
		  Language of the texts ['en', 'es'].
	
	Attributes 
	----------

	list: list
		  Array with collocations.

	Examples
	--------

	>>> from preprocess.grams import Collocations
	>>> from preprocess.demo import preProcessFlow
	>>> from preprocess.data import load_culturalibre
	>>> book = load_culturalibre()
	>>> txt = preProcessFlow(book)
	>>> collocations = Collocations(txt)

	Show the first 10 collocations:

	>>> collocations.head(10)
	[('Cultura', 'libre'),
	('disponible', 'enlace'),
	('dominio', 'público'),
	('Tribunal', 'Supremo'),
	('propiedad', 'intelectual'),
	('propiedad', 'creativa'),
	('dueño', 'copyright'),
	('dueños', 'copyright'),
	('sentido', 'común'),
	('Creative', 'Commons')]

	The results of collocation list is more understandable after ejecute 
	all the preprocessing pipeline.
	
	This class internaly use the function :func:`remove_stopwords`.
	"""
	def __init__ (self,text, ngrams=2, stopwords=True, lang='en'):
		self.text = text
		self.words = []
		self.ngrams = ngrams
		self.lang = lang

		self.grams = {
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
				print("Removing stop words active, to change behavior run:\n \
					Collocations(txt,stopwords=False)")
				self.words = remove_stopwords(self.text, lang=self.lang).split()
			else:
				self.words = self.text.split()
		elif isinstance(self.text,list):
			for file in self.text:
				with open(file) as doc:
					if stopwords:
						print("Removing stop words active, to change behavior run:\n \
					Collocations(txt,stopwords=False)")
						self.words.extend(remove_stopwords(doc.read(), lang=self.lang).split())
					else:
						self.words.extend(doc.read().split())
		
		self.score_fn = self.measures[ngrams].likelihood_ratio

		self.list = self.grams[self.ngrams].from_words(self.words)

	def write(self, path :str):
		"""Write the list of collocations tuples in a txt."""
		with open(path) as doc:
			for element in self.list:
				doc.write(str(element)+'\n')
	
	def head(self, N :int):
		"""Show the first N elements of the collocation list based
		on the score function "likelihood_ratio.
		"""
		return [p for p, s in self.list.score_ngrams(self.score_fn)[:N]]

	def tail(self, N :int):
		"""Show the last N elements of the collocation list based
		on the score function "likelihood_ratio."""
		return [p for p, s in self.list.score_ngrams(self.score_fn)[-N:]]

	#TODO: apply from toolz.curried import compose
	#find_collocations = compose(collocations(),remove_stopwords())
	#Delete the problem to handle to many if/else and manipulate parameters of both