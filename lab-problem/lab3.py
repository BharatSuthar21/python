
#Q1 
"""
1.	Write a function to solve the quadratic equation ax2+bx+c=0. The function should receive a,b and c as input parameters and
A.	Prints the roots 
B.	Return the roots (familiarization with tuples)
"""
"""
def roots_of_equation():
	a=int(input("Enter coffecient of X square : "))
	b=int(input("Enter coffecient of X : "))
	c=int(input("Enter constent term of equation : "))
	d=(-b+(b**2 -(4*a*c))**1/2)/2*a
	e=(-b-(b**2 -(4*a*c))**1/2)/2*a
	return d,e
root=roots_of_equation()
print(root)




# Maam Solution
def quadratic(a,b,c):
	return ((-b+(b**2 -(4*a*c))**1/2)/2*a,(-b-(b**2 -(4*a*c))**1/2)/2*a)
print(quadratic(2,3,4))
"""



















#Q2
# self solve
"""
def eligibility(gender,day,month,year):
	age=2022-year
	if age>=10:
		print("True")
	else:
		print("False")
	return gender,year
	def check_major(gender,day,month,year):
		age=2022-year
		if gender=="female" or gender=="Female":
			if age>=18:
				print("True")
			else:
				print("False")
		else:
			print(" your are not Female")
		return gender,year
major_participant=("female",21,4,2000)
print(major_participant)
participant=eligibility("female",21,12,2002)
print(participant)
"""




"""
def eligibility(gender,day,month,year):
	age=2022-year
	return age>=10
	def check_major(gender,day,month,year):
		gender_check=gender=="female" or gender=="F" or gender=="Female" or gender=="f"
		print(gender_check)
		return age>=18
print(eligibility("male",12,5,2002))
    print(check_major("female",12,6,2000))
"""




"""2A certain sport has the requirement that any female participant
must be a major (age at least 18 years); for males the lower limit
for age is only 10 years. The application procedure filters out any 
applications from candidates below 10 years of age at the very beginning.
However, the constraint for females is checked by a software at a later 
stage. Write a function that receives as input the gender and date of
birth (day, month and year separately) of an applicant and returns 
True if the candidate is eligible, False if not (assume that the 
initial step of ensuring that age is >= 10 years has already been
done). This function calls another function to check if a candidate
is a major based on the day, month and year of birth 
"""
"""

def age(dod_d,dod_m,dod_y):
	return dod_y<2004 or dod_y==2004 and (dod_m<11 or dod_m==11 and dod_d<3)
"""

"""
>>> def age(dod_d,dod_m,dod_y):
...     return dod_y<2004 or dod_y==2004 and (dod_m<11 or dod_m==11 and dod_d<3)
...
>>> age(12,3,2003)
True
>>> age(12,4,2000)
True
>>> age(3,5,1999)
True
"""
"""
def is_eligible(gender,dod_d,dod_m,dod_y):
	return gender=="male"or age(dod_d,dod_m,dod_y)
"""
"""
>>> def is_eligible(gender,dod_d,dod_m,dod_y):
...     return gender=="male"or age(dod_d,dod_m,dod_y)
...j
>>> is_eligible("female",2,3,2002)
True
>>> is_eligible("male",6,3,2062)
True
>>> is_eligible("female",10,8,2070)
False
"""
"""
print(is_eligible("female",2,9,2008))
print(is_eligible("male",2,9,2006))
print(is_eligible("female",2,9,2001))
print(is_eligible("male",3,11,2004))
"""
















#Q3
"""   
3.	Write a function that computes and prints the average 
score of 4 students (2 boys and 2 girls). This function calls
from within two separate functions, one of which receives 
from the user the scores of two boys and returns their 
sum, and the other one does the same for girls 
"""


"""
def boys_score(score1,score2):
	return score1+score2
score3=boys_score(23,45)
def girls_score(score1,score2):
	return score1+score2
score4=girls_score(89,98)
def avg_score():
	return (score3+score4)/4
print(avg_score())
"""




















#Q4

"""
def funcl():
	n=n+2
	x=n+1
n=3
funcl()
print(n)



#UnboundLocalError: local variable 'n' referenced before assignment
#
"""



















#Q5


def func1():
	x=5
	print("Inside func1,before calling func2:",x)#5
	func2()
	print("Inside func1,after calling func2:",x)#20
def func2():
	global x
	x=x*2
x=10
print("Initial:",x)#10
func1()
print("After func1:",x)#5
func2()
print("Ater func2:",x)#40



