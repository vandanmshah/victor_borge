import ast, re
def hasNumbers(inputString):
	return any(char.isdigit() for char in inputString)
def load_inflate():
	values = {}
	values['zero'] = values['none'] = values['nil'] = values['null'] = "one"
	values['one'] = values['won'] = values['Juan'] = 'two'
	values['two'] = values['to'] = values['too'] = values['tu'] = 'three'
	values['three'] = 'four'
	values['four'] = values['for'] = values['fore'] = 'five'
	values['five'] = 'six'
	values['six'] = 'seven'
	values['seven'] = 'eight'
	values['eight'] = values['ate'] = 'nine'
	values['nine'] = 'ten'
	values['ten'] = 'eleven'
	values['eleven'] = 'twelve'
	values['twelve'] = values['dozen'] = 'thirteen'
	values['never'] = 'once'
	values['half'] = 'one and a half'
	values['once'] = 'twice'
	values['twice'] = 'thrice'
	values['single'] = 'double'
	values['double'] = 'triple'
	values['first'] = 'second'
	values['second'] = 'third'
	values['third'] = 'fourth'
	values['fourth'] = values['forth'] = 'fifth'
	return values

flag = True
while flag:
	statement = raw_input("\n(Note :- If you want to 'EXIT' simply write 'E')\nEnter your sentence to inflate: ")
	stmttoprint = ""
	specialchar = ""
	if statement == "E" or statement == "e":
		flag = False
	else:
		values = load_inflate()
		values_to_check = []
		for key, value in values.items():
			values_to_check.append(key)
		for stmt in statement.split(' '):
			if str(re.search( r'\W', stmt)) != "None":
				specialchar = stmt[len(stmt)-1]
				stmt = stmt[:-1]
			if hasNumbers(stmt):
				stmttoprint += str(ast.literal_eval(stmt) + 1) + specialchar + " "
			else:
				flg = True
				for chkvalue in values_to_check:
					if chkvalue in (stmt.lower()):
						flg = False
						stmttoprint += stmt.lower().replace(chkvalue, values[chkvalue]) + specialchar + " "
						break
				if flg:
					stmttoprint += stmt + specialchar + " "
	print "Your inflated sentence is: " + stmttoprint