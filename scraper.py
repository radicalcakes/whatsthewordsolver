import cPickle as pickle
import collections
from bs4 import BeautifulSoup, NavigableString
from urllib2 import urlopen

import redis

r = redis.StrictRedis(host="localhost", port=6379, db=9)

pipe = r.pipeline()
#globals
d = collections.defaultdict(list)


def only_text(l):
	return isinstance(l, NavigableString)

def make_soup(url):
    html = urlopen(url).read()
    return BeautifulSoup(html)

def word_return(m):
	for tag in m.find_all("td"):
		word = tag.string
		if only_text(word) and word[0] != " ":
			w = word.split(" ")
			length = len(w[0])
			full_word = w[0].lower()
			pipe.sadd(length, full_word)
			# d[length].append(full_word)
	pipe.execute()

def scrape():
	urls = [make_soup("http://whats-theword.com/answers/whats-the-word-answers/"),
			make_soup("http://whats-theword.com/answers/whats-the-word-answers-1008-1027/"),
			make_soup("http://whats-theword.com/answers/whats-the-word-answers-1028-1047/"),
			make_soup("http://whats-theword.com/answers/whats-the-word-answers-1048-1056/")]
	for m in urls:
		word_return(m)

	for i in xrange(21, 982, 20):
		st = "http://whats-theword.com/answers/whats-the-word-answers-"+str(i)+"-"+str(i+19)+"/"
		s = make_soup(st)
		word_return(s)


if __name__ == "__main__":
	# summ = 0
	# for k in d:
	# 	summ += len(d[k])
	scrape()
	# print summ
	# print "Letter" in d[6]
	# print "Shield" in d[6]
	# print "Earring" in d[7]
	# print d
	# pickle.dump(d, open( "answers.p", "wb" ) )
