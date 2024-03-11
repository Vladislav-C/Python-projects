#the explanation
print("You will be presented with the character’s original attributes: Force, Health, Wisdom, and Dexterity.")
print("You will need, as in role-playing, to allocate 30 points between skills\n")
guess=None
char=(["1.FORCE",0],
["2.HEALTHS",0],
["3.WISDOM",0],
["4.DEXTERITY",0])
scores=30
while (guess != "3") or (scores != 0):
	for i in range(len(char)):
		print('\t\t',char[i][0],":",char[i][1])
	print('\n\t\t Free point:',scores)
	print(
		'''
What do you want to do now?
                        1. Add points to one of the characteristics.
                        2. Take the points off the record.
                        3. Finish point allocation.
        
        ''')
	guess=input()
	if (scores != 0) and (guess == "3"):
		print("Use all points given to you!\n")
	elif (guess == "1"):
		print("""
			Which characteristic do you want to add points to?
						1.FORCE
						2.HEALTHS
						3.WISDOM
						4.DEXTERITY
			 """)
		key=int(input())
		while ((key-1)<0) or ((key-1)>4):
			print("\nIncorrect data entry!\n")
			key=int(input())
		znach=int(input("Enter the number of points: "))
		while (znach<0) or (znach>scores):
			print("\nIncorrect data entry!\n")
			znach=int(input("Enter the number of points: "))
		cher[key][1]=znach
input()