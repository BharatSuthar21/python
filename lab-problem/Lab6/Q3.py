def vowels_alphabetical(s):
	"""
	Returns : true for vowels in string s are alphabetic order else false

	Value returned has type bool

	Vowels are defined to be 'a','e','i','o' and 'u'.
	Both upper and lower case are treated as same.
	In this there should be "a" or "A" then "e" or 
	"E" then "i" or "E" then "o"or "O" and at last 
	"u" or "U" .In other words, the first occurrence 
	of ‘a’ (if any) appears before first e (if any), 
	first ‘e’ appears before first ‘i’ if any etc. 
	It will return -1 if there is any non letter in s. 


	Parameter s : string for checking
	Precondition : s is a non-empty string
	with only  word

	test code
	>>> vowels_alphabetical("Areiou")
	True

	>>> vowels_alphabetical("reiou")
	True

	>>> vowels_alphabetical("aareiou")
	True

	>>> vowels_alphabetical("arieou")
	False

	>>> vowels_alphabetical("arieou")
	False
	>>> vowels_alphabetical('sky')

	"""

	s=s.lower()
	a=s.find('a')
	e=s.find('e')
	i=s.find('i')
	o=s.find('o')
	u=s.find('u')

	if u==-1:
		u=len(s)
	if o==-1:
		o=u
	if i==-1:
		i=o
	if e==-1:
		e=i
	if a==-1:
		a=0
	return a<=e<=i<=o<=u


if __name__=='__main__':
	import doctest
	doctest.testmod()
