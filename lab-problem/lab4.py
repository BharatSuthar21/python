#Q1
"""
1. Consider the following function definition and the two calls to it.
def func(n=10):
print("Here is the number I received: ",n)
func(5)
func()
Observe the output in each case and try to explain.
"""
"""
def func(n=10):
	print("Here is the number I recived :",n)
func(5)
func()

"""

"""
# Output of the following code is :

(base) PS C:/Users/HPPP/Documents/Python(1st-sem)/lab-problem> python lab4.py
Here is the number I recived : 5
Here is the number I recived : 10

In this we gave default value of n as 10 which is assigned to n when there is no value give to 
parameter n .


"""



#Q2
"""
2. Now consider the following function and the three calls to it:
def func(x,y=10):
print("Sum of the two numbers I received is: ",x+y)
func(3,3)
func(3)
func()
Observe the output in each case and try to explain.
"""
"""
# Out put of the following code is :-

 PS C:/Users/HPPP/Documents/Python(1st-sem)/lab-problem> python lab4.py
the sum of two numbere I received is : 6
the sum of two numbere I received is : 13
Traceback (most recent call last):
  File "C:/Users/HPPP/Documents/Python(1st-sem)/lab-problem/lab4.py", line 35, in <module>
    func()
TypeError: func() missing 1 required positional argument: 'x'
"""

"""
def func(x,y=10):
	print("the sum of two numbere I received is :",x+y)
func(3,3)
func(3)
func()
"""




#Q3
"""
Change the function signature in Q2 as follows and read the error message:
def func(x=10,y):
What do you think it means? Try to explain
"""
"""

def func(x=10,y):
	print("the sum of two numbere I received is :",x+y)
func(3,3)
func(3)
func()
"""
"""
#Output of the following code is :-

 PS C:/Users/HPPP/Documents/Python(1st-sem)/lab-problem> python lab4.py
  File "C:/Users/HPPP/Documents/Python(1st-sem)/lab-problem/lab4.py", line 49
    def func(x=10,y):
                   ^
SyntaxError: non-default argument follows default argument
"""