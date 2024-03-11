scores = []
choice = None
while choice != '0':
	print(
	"""
	0 - Exit 
	1 - Show record 
	2 - Add record 
	"""
	)
	choice = input("Your choice: ")
	if choice == '0':
		print( "Good bye.")
	elif choice == '1':
		print("Records\n")
		print("NAME\tRECORDS")
		for i in scores:
			score,name = i
			print(name,"\t",score)
	elif choice == "2": 
		name = input("Enter player's name: ")
		score = int(input("Enter their record: ")) 
		entry = (score,name) 
		scores.append(entry) 
		scores.sort(reverse=True) 
		scores = scores[:5]
	else:
		print('Sorry, such item-',choice,'is absent')
input("\n\nPress 'Enter' to exit.")