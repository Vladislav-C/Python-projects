import random
#constants
HANGMAN = (
"""
  ------
  |		
  |
  |
  |
  |
  |
  |
  |
 ----------
 """,
 """
  ------
  |		|
  |	
  |
  |
  |
  |
  |
  |
 ----------
 """,
 """
  ------
  |		|
  |		O
  |
  |
  |
  |
  |
  |
 ----------
 """,
 """
  ------
  |		|
  |		O |
  |
  |
  |
  |
  |
  |
 ----------
 """,
 """
  ------
  |		|
  |	  | O |
  |
  |
  |
  |
  |
  |
 ----------
 """,
 """
  ------
  |		|
  |	  | O |
  |		  |
  |		  |
  |
  |
  |
  |
 ----------
 """,
  """
  ------
  |		|
  |	  | O |
  |		  |
  |		  |
  |   |
  |   |
  |
  |
 ----------
 """,
  """
  ------
  |		|
  |	  | O |
  |		  |
  |		  |
  |   |	  |
  |   |	  |
  |
  |
 ----------
 """)
MAX_WRONG = len(HANGMAN)-1
WORD = ('ophthalmologist',
'cellar',
'drama',
'publisher',
'translator',
'taffy',
'guard',
'sham',
'baroque',
'abbreviation',
'illustration')
#variable initialization
word = random.choice(WORD)	#echo word
word = word.upper()
word_guess = '-' * len(word) #one FIS per letter
wrong = 0
used = [] #letters that the player already offered
print("Welcome to the 'Gallows' game. Good luck!")
while (wrong != MAX_WRONG) and (word_guess != word):
	print(HANGMAN[wrong])
	print("\nYou’ve already offered the following letters:\n",used)
	print("\nThe guessed word now looks like this:\n",word_guess)
	guess = input("\n\nEnter a letter: ")
	guess = guess.upper()
	while guess in used:
		print("You've already entered this letter")
		guess = input("\n\nEnter a letter: ")
		guess = guess.upper()
	used.append(guess)
	if guess in word:
		print("\nYes! The letter",guess,"is in the word.")
		new = ""
		for i in range(len(word)):
			if guess == word[i]:
				new += guess
			else :
				new += word_guess[i]
		word_guess = new
	else:
		print("\nUnfortunately, the letter",guess,"is absent.")
		wrong+=1
if wrong == MAX_WRONG:
	print(HANGMAN[wrong])
	print("\nYou hang!")
else:
	print('You guessed!')
print("\nThe word has been chosen",word)
input("\n\nPress 'Enter' to exit.")
