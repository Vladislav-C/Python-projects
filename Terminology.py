geek = {"404": "Do not know. Do not own information. From error message 404 'Page not found'.",
		"Googling": "'Googling', a web of information about someone.",
		"Keyboard Pl aque" : "Trash that accumulates in the keyboard of the computer.",
		 "Link Rot" : "The process of obsolescence of hyperlinks on web pages.",
		 "Percussive Maintenance" : "About the situation when someone hits the body of a faulty electronic device in the hope of restoring its operation.",
		 "Uninstalled" : "About the dismissal of someone, Especially popular at the turn of the 1990-2000. "} 
choice = None
while choice != '0':
	print(
	"""
	О - Exit 
	1 - Interpret a term
	2 - Add a term
	3 - Change a term
	4 - Delete a term
	"""
	)
	choice = input("Your choice: ")
	print()
	#exit
	if choice == '0':
		print('Good bye.')
	elif choice == '1':
		term = input('What term do you want to know ?')
		print(geek.get(term,'Unfortunately, there is no such term.'))
	elif choice == '2':
		term = input('What term do you enter ?')
		if term not in geek:
			definition = input('\nEnter the interpretation: ')
			geek[term] = definition
			print('\nThe term',term,'has been added.')
		else:
			print('\nSuch a term already exists! Try to change its interpretation.')
	elif choice == '3':
		term = input('What term do you override ?')
		if term in geek:
			definition = input('\nEnter the interpretation: ')
			geek[term] = definition
			print('\nThe term',term,'has been overriden.')
		else:
			print('\nThere is no such term! Try adding it.')
	elif choice == '4':
		term = input('Which term to delete ?')
		if term in geek:
			del geek[term]
			print('\nThe term',term,'has been deleted.')
		else:
			print('\nThere is no such term')
	else:
		print('Sorry such choice-',choice,'is absent')
input("\n\nPress 'Enter' to quite.")
