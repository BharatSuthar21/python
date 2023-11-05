
"""
Demonstring a procedure definition

Author: Bharat Suthar
Date : 1/12/2022
"""
def find_chronology(time1,suffix1,time2,suffix2):
	"""
	Print the time of event 1 as before or after or same ,
	after comparing first two parameter with last two parameter 

	This program takes four parameters and 1st and 3rd parameter 
	is of int type and 2nd and 4th parameter is of string type. 

	Parameter time1:Event1st time
	Precondition : time1 is a non-empty int
	Parameter suffix1:Event1st suffix as  "am" or "pm"
	Precondition : suffix1 is a non-empty str
	Parameter time2:Event2 time
	Precondition : time2 is a non-empty int
	Parameter suffix2:Event2nd suffix as "am" or "pm"
	Precondition : suffix2 is a non-empty str



	Test code:-

	>>> find_chronology(12,"am",12,"pm")
	'Before'
	>>> find_chronology(1,"am",2,"am")
	'Before'
	>>> find_chronology(5,"pm",2,"am")
	'After'
	>>> find_chronology(5,"am",2,"pm")
	'Before'
	>>> find_chronology(4,'am',3,'am')
	'After'


	"""
	suffix1=suffix1.lower()
	suffix2=suffix2.lower()

	if suffix1=='am' and suffix2=='pm':
		return 'Before'
	elif suffix2=='am' and suffix1=='pm':
		return 'After'
	elif suffix1==suffix2:
		if time1>time2:
			return'After'
		elif time1<time2:
			return 'Before'
		else:
			return 'Same'
if __name__=='__main__':
	import doctest
	doctest.testmod()
