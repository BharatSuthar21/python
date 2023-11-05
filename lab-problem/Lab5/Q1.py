
"""
Demonstring a procedure definition

Author: Bharat Suthar
Date : November 12,2022
"""
def find_chronology(time1,suffix1,time2,suffix2):
	"""
	Print the time of event 1 as before or after or same ,
	after comparing first two parameter with last two parameter 

	This program takes four parameters and 1st and 3rd parameter 
	is of int type and 2nd and 4th parameter is of string type. 







"""
def find_chronology(time1,suffix1,time2,suffix2):
	Before=true==time1>time2 
	print("Before")
	same=true==(time1==time2)
	print("same")
	after=true==time1<time2
	print("After")
a=find_chronology(12,"am",12,"pm")
print(a)
"""
	
def find_chronology(time1,suffix1,time2,suffix2):
	Before=True==time1>time2
	print(Before)
	Same=True==(time1==time2)
	print(Same)
	After=True==time1<time2
	print(After)
find_chronology(12,"am",12,"pm")

"""
 Print time of event

 This program is about to tell that weater the 
 event is going to happen at what time in means of 
 "before","Same"and "After".  It will print before 
 if time1>time2 and same if time1==time2 and after if 
 time1<time2 .It will also check the suffix of then 
 time that has been assigned to time1 and time2 

 Parameter time1:Event1st time
 Precondition : time1 is a non-empty int

 Parameter suffix1:Event1st suffix as  "am" or "pm"
 Precondition : suffix1 is a non-empty str

 Parameter time2:Event2 time
 Precondition : time2 is a non-empty int

 Parameter suffix2:Event2nd suffix as "am" or "pm"
 Precondition : suffix2 is a non-empty str

 Test code
 >>>find_chronology(12,"am",12,"pm")
 >>>same

 >>>find_chronology(1,"am",2,"am")
 >>>Before

 >>>find_chronology(5,"am",2,"am")
 >>>After

>>>find_chronology(5,"pm",2,"am")
 >>>After

>>>find_chronology(5,"am",2,"pm")
 >>>After


