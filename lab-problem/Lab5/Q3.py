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

	>>>unique_vowels_in_words("Cricketout")
	>>>4

	>>>unique_vowels_in_words("ICricketout")
	>>>5

	>>>unique_vowels_in_words("sky")
	>>>0

	>>>unique_vowels_in_words("see")
	>>>1

	>>>unique_vowels_in_words("Cricketout2")
	>>>-1

	>>>unique_vowels_in_words("Cricketout",True)
	>>>4
    
    >>>unique_vowels_in_words(" I will play Cricketout",True)
	>>>7

	>>>unique_vowels_in_words("Sky",True)
	>>>0

	>>>unique_vowels_in_words("Cricketout1",True)
	>>>-1

	>>>unique_vowels_in_words("seE",True)
	>>>2
	"""
