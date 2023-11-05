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
	True

	>>> palindrome_check("abcddca")
	False

    >>> palindrome_check("abcdcba")
	True

	>>> palindrome_check("abcddcba1")
	-1

