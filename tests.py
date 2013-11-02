#do imports for actual code here
import re
import whatsthewordsolver
from bs4 import BeautifulSoup, NavigableString

from whatsthewordsolver import return_inputs, return_clue, return_num

from scraper import make_soup

#test user input
def test_clue(s):
	return len(s) == 11

def test_num(n):
	return isinstance(n, int) and n < 9 and n >= 3

def only_text(l):
	return isinstance(l, NavigableString)


if __name__ == "__main__":
	#test something out
	d = {4:["fuck", "luck", "suck", "guck"]}
	l = "lrekxugnc"

	#O(n^2) we can optimize this algo later
	for word in d[4]:
		s = ""
		for char in word:
			if char in l:
				s += char
		if len(s) == 4:
			print s
		
	print test_clue("fiefnloewns") == True
	print test_clue("ddfsalkjdflsajlk") == False
	print test_num(4) == True
	print test_num(9) == False
	# print return_inputs(return_clue, return_num)
	# m = make_soup("http://whats-theword.com/answers/whats-the-word-answers/")
	# for l in m.find_all("td"):
	# 	i = l.string
	# 	if only_text(i) and i[0] != " ":
	# 		print i


	# for i in xrange(21, 982, 20):
	# 	print i, i+19

	# 	"http://whats-theword.com/answers/whats-the-word-answers-1008-1027/"
	# 	"http://whats-theword.com/answers/whats-the-word-answers-1028-1047/"
	# 	"http://whats-theword.com/answers/whats-the-word-answers-1048-1056/"


