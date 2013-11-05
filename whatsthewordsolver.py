import cPickle as pickle
import redis

r = redis.StrictRedis(host="localhost", port=6379, db=9)

d = pickle.load(open("answers.p", "rb"))

def is_letters(s):
	#ensures letters are whatstheword standards
	if len(s) == 11:
		return True

def is_len(n):
	return isinstance(n, int) and n < 9 and n >= 3


def return_clue():
	#returns tuple of inputs if true
	clue = raw_input("Enter letters with no spaces: ")
	while not is_letters(clue):
		print "Oops! You did not enter the correct amount of letters.\n"
		clue = raw_input("Enter letters with no spaces: ")
	return clue

def return_num():
	num = int(raw_input("Enter length of clue: "))
	while not is_len(num):
		print "Oops! Clues are only 3 to 8 letters.\n"
		num = int(raw_input("Enter length of clue: "))
	return num

def return_inputs(c,n):
	return c(), n()

# def finder(tup):
# 	for word in d[tup[1]]:
# 		s = ""
# 		for char in word:
# 			if char in tup[0]:
# 				s += char
# 		if len(s) == tup[1]:
# 			print s


def redis_finder(tup):
	answers = r.smembers(tup[1])
	for word in answers:
		print word

if __name__ == "__main__":
	redis_finder(return_inputs(return_clue,return_num))