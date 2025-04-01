#Python file for the main process

from game import *							#Imports everything from the game.py
import os 									#Imports os library
clear_Screen()

def Difficulty():							#Asks and sets the difficulty
	clear_Screen()
	while True:
		print("="*42)
		print("\n"+f"{'[CHOOSE DIFFICULTY]':^42}"+"\n")
		print(f"{'[1] EASY ':^14}"f"{'[2] MEDIUM':^14}"f"{'[3] HARD ':^14}")
		print(f"{'50% QUOTA':^14}"f"{'75% QUOTA':^14}"f"{'100% QUOTA':^14}")
		print(f"{'3 COUNTERS':^14}"f"{'4 COUNTERS':^14}"f"{'5 COUNTERS':^14}")
		print("\n"+"="*42)
	
		diff = input("\nEnter choice here: ")

		if diff == "1":
			return "EASY"
		elif diff == "2":
			return "MEDIUM"
		elif diff == "3":
			return "HARD"
		else: 
			os.system('cls')
			print("Invalid Input!")

def Main_Menu():							#Prints the main menu
	print("Welcome to the Noodle Shop Game!")
	print("[1] PLAY")
	print("[2] VIEW HIGHSCORE")
	print("[3] HOW TO PLAY")
	print("[4] QUIT")

def save_Score(record):						#Saves the score to an external txt file
	f = open("records.txt", "a")			#Opens the txt file for the scores

	f.write(str(record[0])+","+record[1]+","+str(record[2])+","+record[3]+"\n")		#Writes the final score, name, rounds and dificulty in one line respectively
	#writes the score, name, rounds, and difficulty in a file

	f.close()								#Closes the txt file for the scores

def load_Scores():							#Unloads the score from the txt file
	f = open('records.txt','r')				#Opens the txt file for the score
	new_records = []						#Container for the recorded redords from the previous games.
	sorting = []							#Container for the sorted scores
	for line in f:
		token = line[:-1].split(',')		#Splits the records
		list1 = [int(token[0]),token[1],token[2],token[3]]		#List for score,name,rounds, and difficulty
		new_records.append(list1)			#Adds the splitted records to the new records
		sorting.append(int(token[0]))		#Adds the score to the sorting list.
	sorting.sort(reverse=True)				#Sorts each score in descending order
	f.close()								#Closes the txt file for the scores
	return [new_records,sorting]

def print_Loaded(values):					#Prints the unpacked records
	if len(values[0]) == 0:					#Checks whether there are no existing records
		print("There are no existing records.")
	else:									#Prints the records
		print("%-15s %-15s %-15s %-15s %s"%("Rank","Score","Name","Rounds","Difficulty"),"\n")
		rank = 1
		for each in values[1]:
			for element in values[0]:
				if each == element[0]:
					print("%-15s %-15s %-15s %-15s %s"%(rank,element[0],element[1],element[2],element[3]))
					rank+=1
					values[0].remove(element)

def name_Input():							#Asks for the name and returns it as a value
	clear_Screen()
	while True:
		name = input("Enter your name? (Must be 1 to 10 characters)\n")		#System will only accepts names less than 11 characters
		if len(name)>11:
			print("Your name exceeded 10 characters.")
		elif len(name)<1:
			print("Your name must be at least 1 character.")
		else:
			return name

def guidelines():								#Prints the guidelines for the game
	line_groups=[6,10,9,10,12,5,7,14]			#Line groups to print at a time
	f = open('tutorial.txt','r')				#Opens the txt file for the guidelines
	for x in range(0,8):
		clear_Screen()
		for y in range(0,line_groups[x]):
			print(f.readline())
		if x != 7:
			placeholder = input("Press ENTER to Proceed")
	f.close()									#Closes the txt fiel for the guidelines

#mainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainmainloop
def main():
	while True:
		Main_Menu()
		main_action = input("Enter choice: ")		#Asks for the main action of the game

		if main_action == "1":
			name = name_Input()						#Stores the name
			diff = Difficulty()						#Stores the difficulty chosen
			print("\n"+"You picked", diff)
			placeholder = input("Press Enter to continue.")

			record = game_Function(name,diff,trays,counters)		#Carries out the game function and records the score, name, rounds and difficulty
			save_Score(record)						#Saves the records to the respective txt file

		elif main_action == "2":
			clear_Screen()
			print_Loaded(load_Scores())				#Prints the records
			placeholder = input("\nPress Enter to go back")
			clear_Screen()

		elif main_action == "3":
			clear_Screen()
			guidelines()							#Prints the guidelines
			placeholder = input("\nPress Enter to quit tutorial")
			clear_Screen()

		elif main_action == "4":
			print("Thank you for playing!")			#Exits the code.
			break
		
		else:
			clear_Screen()
			print("Invalid input.")
			print("")
			
if __name__ == "__main__":
	print("Please open the console in full screen for best experience")
	input("Press Enter to continue...")
	clear_Screen()
	main()