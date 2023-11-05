def roots_of_equation():
	a=int(input("Enter coffecient of X square : "))
	b=int(input("Enter coffecient of X : "))
	c=int(input("Enter constent term of equation : "))
    return ((-b+-(b**2 -(4*a*c))**1/2)/2*a)
root=roots_of_equation()
print(roots)
