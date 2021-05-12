day = input("Enter the day for which you need to know the timings: ")
if day == "Monday" or  day=="Tuesday" or day=="Wednesday" or day=="Thursday" or day=="Friday":
	print("9.00AM to 6.00PM")
elif day == "Saturday":
	print("9.00AM to 1.00PM")
elif day == "Sunday":
	print("Holiday")
else:
	print("it's an invalid input")
