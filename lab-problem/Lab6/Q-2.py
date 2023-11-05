def unique_vowels_in_words(s,case_sensitive=False):


	"""
	Return :no of unique vowels in  string s in different condition

	Value returned is int type

	Vowels are defined to be 'a','e','i','o' and 'u'.
	In this function we count number of unique vowels .
	Upper-case ‘A’and lower-case ‘a’ will be considered 
	as the same if case_sensitive is False (default case)
	otherwise it will consider them different.
	It will also return -1 if string contain any non 
	string in s .

	Parameter s :the text to check for unique vowels
	Precondition : s is a non empty string 

	Parameter case_sensitive: It check upper and lower case 
	Precondition : case_sensitive it has its default vale False 
	    And can be provided with other vale but not empty value

	Test case     

	>>> unique_vowels_in_words("Cricketout")
	4

	>>> unique_vowels_in_words("ICricketout")
	4

	>>> unique_vowels_in_words("sky")
	0

	>>> unique_vowels_in_words("see")
	1

	>>> unique_vowels_in_words("Cricketout2")
	-1

	>>> unique_vowels_in_words("Cricketout",True)
	4
    
    >>> unique_vowels_in_words(" I will play Cricketout",True)
	-1

	>>> unique_vowels_in_words("Sky",True)
	0

	>>> unique_vowels_in_words("Cricketout1",True)
	-1

	>>> unique_vowels_in_words("seE",True)
	2
	"""
	vowels='aeiouAEIOU'
	if s.isalpha()==False:
		print('-1')
	elif case_sensitive==False:
		s=s.lower()
		a=(int('a'in s))
		e=(int('e'in s))
		i=(int('i'in s))
		o=(int('o' in s))
		u=(int('u' in s))
		return a+e+i+o+u

	else:
		lower_unique_vowels=(int('a'in s)+int('e'in s)+int('i'in s)+int('o' in s)+int('u' in s))
		upper_unique_vowels=(int('A'in s)+int('E'in s)+int('I'in s)+int('O' in s)+int('U' in s))
		return lower_unique_vowels+upper_unique_vowels
if __name__=='__main__':
	import doctest
	doctest.testmod()
