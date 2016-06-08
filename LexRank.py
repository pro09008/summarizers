import argparse
from _summarizer import AbstractSummarizer

class LexRankSummarizer(AbstractSummarizer):
	"""
	LexRank: Graph-based Centrality as Salience in Text Summarization
	Source: http://tangra.si.umch.edu/~radev/lexrank/lexrank.pdf
	"""

	def __call__(self,document,sentences_count):
		sentences_words=[self._to_words_set(s) for s in document.sentences]
		tf_metrics=self._compute_tf(sentences_words)


	def _to_words_set(self,sentence):
		words=map(self.normalize_word,sentence.words)
		return [self.stem_word(w) for w in words if w not in self._stop_words]


	def _compute_tf(self,sentences):
		tf_values=map(Counter,sentences)

		tf_metrics=[]
		for sentence in tf_values:
			metrics={}
			max_tf=self._find_tf_max(sentence)
 	
			for term,tf in sentence.items():
				metrics[term]=tf/max_tf

			tf_metrics.append(metrics)

		return tf_metrics

	@staticmethod
	def _find_tf_max(terms):
		return max(terms.values()) if terms else 1

	@staticmethod
	def _compute_idf(sentences):
		idf_metrics={}
		sentences_count=len(sentences)
		




def main():
	args=argparse.ArgumentParser()
	args.add_argument('sentences',help='file of line-separated sentences to summarize')
	args.parse_args()

	text=LexRankSummarizer()
	text


if __name__=='__main__':
	main()