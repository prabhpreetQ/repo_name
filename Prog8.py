def div():
	a=int(raw_input("enter a dividend : "))
	b=int(raw_input("enter a divisor : "))
	try:
		div=a/b
	except ZeroDivisionError as e:
		return("Don't divide by zero:",e)
	return div

print div()