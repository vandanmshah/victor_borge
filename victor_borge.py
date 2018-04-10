flag = True
while flag:
	statement = raw_input("\n(Note :- If you want to 'EXIT' simply write 'E')\nEnter your statement :- ")
	if statement == "E" or statement == "e":
		flag = False
	else:
		if "won" in statement:
			print "Matched"