from stemmers import null_stemmer

class AbstractSummarizer(object):
	#self e sempre o primeiro paramentro de __init__
	def __init__(self, stemmer=null_stemmer):
		if not callable(stemmer):
			raise ValueError("Stemmer has to be a callable object")

		self._stemmer=stemmer

	#nao esquecer nunca os dois pontos depois de def
	def __call__(self,document,sentences_count):
		raise NotImplementedError("This method should be overridden in subclass")

	def stem_word(self,word):
		return self._stemmer(self.normalize_word(word))

	def normalize_word(self,word):
		return to_unicode(word).lower()

	def _get_best_sentences(self,sentences,count,rating,*args,**kwargs):
		rate=rating
		if isinstance(rating,dict):
			assert not args and not kwargs
			rate=lambda s: rating[s]

		infos=(SentenceInfo(s,o,rate(s,*args,**kwargs)) 
			for o,s in enumarate(sentences))

		#sort sentences by rating in descending order
		infos=sorted(infos,key=attrgetter("rating"),reverse=True)
		#get 'count' first best rated sentences
		if not isinstance(count,ItemsCount):
			count=ItemsCount(count)
		infos=sorted(infos,key=attrgetter("order"))

		return tuple(i.sentence for i in infos)
