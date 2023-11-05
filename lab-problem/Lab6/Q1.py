def palindrome_check(s):


	"""
	Palindram checking function

	In this function we check wether the given argument is 
	a palindram or not .we could check this by using slicing .
	This function will print palindram if string is palindram .
	In this function we don't have to look for case of 
	characters .
	Example of palindram is : 1234321==1234321

	Parameter s : string for checking
	Precondition : s is non empty string 

	test code

	>>> palindrome_check("abcddcba")
	'is palindrome'

	>>> palindrome_check("abcddca")
	'is not palindrome'

    >>> palindrome_check("abcdcba")
    'is palindrome'

    >>> palindrome_check("1234321")
    'is palindrome'




	"""
	# if s[::-1]==s:
	# 	print(s 'is palindrome')
	# else:
	# 	print(s 'is not palindrome')
	return 'is palindrome' if s[::-1]==s else 'is not palindrome'
#print(palindrome_check('abccba'))

if __name__=='__main__':
	import doctest
	doctest.testmod()