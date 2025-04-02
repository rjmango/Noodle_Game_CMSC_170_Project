#Module for the game functions

import random
import os
import shutil
import improvedAI

counters = {}																	# Counter:[noodle preference, patience]
trays = {'A':[0,0],'B':[0,0],'C':[0,0], 'D':[0,0], 'E':[0,0], 'F':[0,0]}		# Tray:[Occupied, noodle doneness]
aiCounters = {}																	# Counter:[noodle preference, patience]
aiTrays = {'A':[0,0],'B':[0,0],'C':[0,0], 'D':[0,0], 'E':[0,0], 'F':[0,0]}

def Game_Menu(Prompt):											#Print game Menu
	COL_WIDTH =  int(shutil.get_terminal_size().columns // 2) - 3
	print("1 - PLACE noodle bowl in the tray".ljust(COL_WIDTH) + ' | ' + Prompt.ljust(COL_WIDTH))
	print("2 - SERVE noodle bowl".ljust(COL_WIDTH) + ' | ' + "".ljust(COL_WIDTH))
	print("3 - DISCARD noodle bowl in the tray".ljust(COL_WIDTH) + ' | ' + "".ljust(COL_WIDTH))
	print("4 - WAIT and skip a turn".ljust(COL_WIDTH) + ' | ' + "".ljust(COL_WIDTH))
	print("If display is not properly shown, please input R to refresh")
	print("Once action is chosen (Place, Serve, or Discard),\ninput \"CANCEL\" to cancel the operation")

def counter_Preparation(diffi,counters, aiCounters):					#Prepare number of counters based on difficulty and returns the score multiplier
	letters = "ABCDEF"
	if diffi == "EASY":
		x = 3
		for k in range(0,x):
			counters[letters[k]] = [0,""]
			aiCounters[letters[k]] = [0,""]
		return 1
	elif diffi == "MEDIUM":
		x = 4
		for k in range(0,x):
			counters[letters[k]] = [0,""]
			aiCounters[letters[k]] = [0,""]
		return 2
	elif diffi == "HARD":
		x = 5
		for k in range(0,x):
			counters[letters[k]] = [0,""]
			aiCounters[letters[k]] = [0,""]
		return 3

def Patience(x):											#Returns a number of patience for each order depending on the preference
	if x == 1:
		return random.randint(5,8) #dipped
	if x == 2:
		return random.randint(6,9) #extra firm
	if x == 3:
		return random.randint(7,10) #firm
	if x == 4:
		return random.randint(8,11) #regular
	if x == 5:
		return random.randint(9,12) #soft
	if x == 6:
		return random.randint(10,13) #extra soft
	if x == 7:
		return random.randint(10,14) #overcooked
	else:
		return "" 		

def counter_System(counters,vals):							#System for the counters
	list_counter=[k for k in counters.keys()]
	for c in list_counter:									#Decrease patience of each customer counter is taken
		if counters[c][0] != 0:
			counters[c][1] -= 1

		if counters[c][0] == 0 and vals["count"] != vals["total"]:		#Adds new customer when a counter is empty and there are still customers yet to serve
			counters[c][0] = random.randint(0,7)
			counters[c][1] = Patience(counters[c][0])
			if counters[c][0] != 0:
				vals["count"] += 1

def unsuccessful_Order(counter,streak):					#Function for updating counters when customers patience reach zero
	x = 0
	emptyCounter = ""
	list_counter=[k for k in counter.keys()]
	for c in list_counter:									#Resets the counter into default when order is unsuccessful
		if counter[c][0] != 0 and counter[c][1] == 0:
			counter[c] = [0,""]
			streak["current"] = 0
			x = 1
			emptyCounter += (f"{c}, ")
	return "" if x == 0 else f"WARNING! Customer at Counter {emptyCounter[:-2]} walked away!"

def print_Subcounter(subcounter):								#Prints the counter
	COL_WIDTH =  int(shutil.get_terminal_size().columns // 2) - 3
	Noodle_Preference={0:"Empty",
					   1:"Dipped",
					   2:"Extra_Firm",
					   3:"Firm",
					   4:"Regular",
					   5:"Soft",
					   6:"Extra_Soft",
					   7:"Overcooked"}
	
	if subcounter == '':
		return

	left = ""
	right = ""
	for counter in subcounter:								#Prints customer preference or when empty
		playerValue = counters[counter]
		aiValue = aiCounters[counter]
		left += f"{Noodle_Preference[playerValue[0]]:^25}"
		right += f"{Noodle_Preference[aiValue[0]]:^25}"
	print(left.ljust(COL_WIDTH) + ' | ' + right.ljust(COL_WIDTH))
	
	out = ""
	for counter in subcounter:								#Visual design for each counter
		out += f"{'-----------':^25}"
	print(out.ljust(COL_WIDTH) + ' | ' + out.ljust(COL_WIDTH))

	left = ""
	right = ""
	for counter in subcounter:								#Print counter name
		left += f"{'Counter '+counter:^25}"
		right += f"{'Counter '+counter:^25}"
	print(left.ljust(COL_WIDTH) + ' | ' + right.ljust(COL_WIDTH))

	left = ""
	right = ""
	for counter in subcounter:								#Prints patience when there is a customer
		playerValue = counters[counter]
		aiValue = aiCounters[counter]
		if playerValue[0] == 0:									
			left += f"{'':^25}"
		else:
			left += f"{'Patience: '+str(playerValue[1]):^25}"
		if aiValue[0] == 0:
			right += f"{'':^25}"
		else:			
			right += f"{'Patience: '+str(aiValue[1]):^25}"
	print(left.ljust(COL_WIDTH) + ' | ' + right.ljust(COL_WIDTH))	
	print_NextLine()
		
def input_Tray(trays):										#Function for inputing trays
	while True:
		Tray_input = input("Choose TRAY to PLACE: ")
		if Tray_input == "CANCEL":
			return True
		if Tray_input.upper() in trays:						#Checks whether tray is occupied
			if trays[Tray_input.upper()][0] == 1:
				print("Tray is already occupied")
			else:
				trays[Tray_input.upper()][0] = 1 			#Update status from 0/empty to 1/occupied
				break
		else:
			print("Invalid Input!")
	return False

def discard_Tray(trays):									#Function for discarding trays
	while True: 
		Tray_input = input("Choose TRAY to DISCARD: ")
		if Tray_input == "CANCEL":
			return True
		if Tray_input.upper() in trays:						#Checks whether tray is empty
			if trays[Tray_input.upper()][0] == 0:
				print("Tray is already empty")
			else:
				trays[Tray_input.upper()] = [0,0]			#Resets tray into default status
				break
		else:
			print("Invalid Input!")
	return False

def increment_Tray(trays):									#Increments each tray when occupied
	for v in trays.values():
		if v[0] == 1:										#Checks if tray is occupied
			if v[1] == 7:									#Checks if noodle is overcooked
				pass
			else:
				v[1] += 1

def print_Subtray(subtray):										#Prints each tray
	COL_WIDTH =  int(shutil.get_terminal_size().columns // 2) - 3
	Noodle_Doneness={"0":"Empty",
				  	 "1":"Dipped",
					 "2":"Extra Firm",
					 "3":"Firm",
					 "4":"Regular",
					 "5":"Soft",
					 "6":"Extra Soft",
					 "7":"Overcooked"
					}
	left = ""
	right = ""
	for tray in subtray:								#Visual design for each counter
		playerDoneness = Noodle_Doneness[str(trays[tray][1])]
		aiDoneness = Noodle_Doneness[str(aiTrays[tray][1])]
		left += f"{playerDoneness:^25}"
		right += f"{aiDoneness:^25}"
	
	print(left.ljust(COL_WIDTH) + ' | ' + right.ljust(COL_WIDTH))

	out = ""
	for tray in subtray:								
		out += f"{'-----------':^25}"
	print(out.ljust(COL_WIDTH) + ' | ' + out.ljust(COL_WIDTH))

	left = ""
	right = ""
	for tray in subtray:								
		left += f"{'Slot: ' +tray:^25}"
		right +=  f"{'Slot: ' +tray:^25}"
	print(left.ljust(COL_WIDTH) + ' | ' + right.ljust(COL_WIDTH))
	print_NextLine()

def counter_Empty(counters):								#Checks whether counter is emtpy
	list_counter=[k for k in counters.keys()]
	for c in list_counter:
		if counters[c][0] != 0:
			return False
	return True	

def tray_Full(trays):										#Checks whether tray is full
	list_tray=[k for k in trays.keys()]
	for t in list_tray:
		if trays[t][0] != 1:
			return False
	return True 

def tray_Empty(trays):										#Checks whether tray is empty
	list_tray=[k for k in trays.keys()]
	for t in list_tray:
		if trays[t][0] != 0:
			return False
	return True 

def empty_Tray(trays):										#Empties all tray slots
	for k in trays.keys():
		trays[k]=[0,0] 										#Resets each tray slot into its default values

def main_Action(trays,counters,vals,quota,streak,diffi,name):	#Function for choosing main action in game
	while True:
		action = input("\nChoose action: ")
		if action == "1":									# Place Noodle
			if tray_Full(trays) == False:					#Checks if tray is not full
				return input_Tray(trays)							#Inputs a tray in slot
			else:
				print("Tray is full")
		elif action == "2":									# Serve Noodle
			if counter_Empty(counters) == True:				# Checks if all counters are empty
				print("There are no customers to serve!")
			elif tray_Empty(trays) == True:					# Checks if all trays are empty
				print("All of the tray slots are empty! You need to place a noodle bowl first.")
			else:
				return serve(trays,counters,vals,quota,streak)		# Serves a selected tray slot to a selected counter
		elif action == "3":									# Discard Noodle
			if tray_Empty(trays) == False:					# Checks if all trays are not empty
				return discard_Tray(trays)					# Empties a tray in slot
			else:
				print("Tray is already empty")
		elif action == "4":									# Wait
			return False
		elif action == "R" or action == "r":
			return True
		else:
			print("Invalid Action!")

def Quota(diffi,vals):										#Returns the quota depending on the difficulty
	if diffi == 'EASY':
		return int(vals["total"]*0.5)
	if diffi == 'MEDIUM':
		return int(vals["total"]*0.75)
	else:
		return vals["total"]

def serve(trays,counters,vals,quota,streak):				#Function for serving
	while True:												#Tray Entry
		pick_tray = input("Enter TRAY slot: ")
		if pick_tray.upper() == "CANCEL":
			return True
		if pick_tray.upper() in trays:
			if trays[pick_tray.upper()][0] == 0:
				print ("Tray slot is empty")
			else:
				break
		else: print("Invalid Input!")

	while True:												#Counter Entry
		pick_counter = input("Enter COUNTER to SERVE: ")
		if pick_counter.upper() in counters:
			if counters[pick_counter.upper()][0] == 0:
				print("Counter is empty")
			else: 
				break
		else: print("Invalid Input!")

	if trays[pick_tray.upper()][1] == counters[pick_counter.upper()][0]:	#Checks if customer preference is equal to the doneness of noodle served
		print("\nOrder Success!")
		vals["served"] += 1 														#Adds one to successful order count
		vals["score"] += int(35 + 0.15*streak["current"])									#Adds score rounded down to nearest integer. Score dedpends on the streak
		streak["current"] += 1
		if streak["current"] > streak["longest"]:
			streak["longest"] = streak["current"]											#Updates the maximum streak
	else:
		print("\nOrder Unsuccesful")
		if vals["score"] > 10:													#Score cannot be negative
			vals["score"] -= 10													#Subtracts score when order unsuccesful
		streak["current"] = 0 													#Resets streak

	trays[pick_tray.upper()] = [0,0]										#Resets the default value for the selected tray
	counters[pick_counter.upper()] = [0,""]									#Resets the defaul value for the selected counter
	return False

def game_Over(name,diffi,total,vals,multiplier,streak):						#Prints the journey of the customer when game over
	clear_Screen()
	print("Summary of", name+"'s journey","\n")
	print("="*45)
	print("Difficulty:", diffi)
	print("Total number of customers:", total["count"])
	print("Total number of successful orders:", total["served"])
	print("Longest Streak:",streak["longest"])
	print("Total number of rounds:", vals["rounds"])
	print("Final Score:",vals["score"]*multiplier)
	print("="*45 + "\n")
	placeholder = input("Press Enter to continue.")
	clear_Screen()

def generateCustomers(totalCustomers):
	return [random.randint(1, 7) for _ in range(totalCustomers)]	#Generates a list of customers with random preferences

def print_Header(string):
	COL_WIDTH =  int(shutil.get_terminal_size().columns // 2) - 3
	print_NextLine()
	out = string.center(25)
	print(out.ljust(COL_WIDTH) + ' | ' + out.ljust(COL_WIDTH))
	print_NextLine()

def print_NextLine():
	COL_WIDTH =  int(shutil.get_terminal_size().columns // 2) - 3
	print("".ljust(COL_WIDTH) + ' | ' + "".ljust(COL_WIDTH))

def print_Border():
	COL_WIDTH =  int(shutil.get_terminal_size().columns // 2) - 3
	print("="*(COL_WIDTH+1)+"|"+"="*(COL_WIDTH+4))

def clear_Screen():
	if os.name == 'nt':  # Windows
		os.system('cls')
	else:  # Mac and Linux
		os.system('clear')


def print_Display(name,diffi,vals,quota,streak, aivals, aistreak):							#Prints the Display
	COL_WIDTH =  int(shutil.get_terminal_size().columns // 2) - 3
	# Prints the names of both player and AI
	print(name.ljust(COL_WIDTH) + ' | ' + "AI".ljust(COL_WIDTH))
	
	# Prints the score and streak of both player and AI
	left = (f'{("Score: "+str(vals["score"])).ljust((COL_WIDTH//2))}'
		 	f'{("Streak: "+str(streak["current"])).rjust(COL_WIDTH//2)}')
	right = (f'{("Score: "+str(aivals["score"])).ljust((COL_WIDTH//2))}'
		  	 f'{("Streak: "+str(aistreak["current"])).rjust(COL_WIDTH//2+3)}')
	print(left.ljust(COL_WIDTH) + ' | ' + right.ljust(COL_WIDTH))

	# Prints the customers to serve and successful orders of both player and AI
	left = (f'{("Customers to serve: "+str(vals["total"]-vals["count"])).ljust((COL_WIDTH//2))}'
		    f'{("Successful Orders: "+str(vals["served"])).rjust(COL_WIDTH//2)}')
	right = (f'{("Customers to serve: "+str(aivals["total"]-aivals["count"])).ljust((COL_WIDTH//2))}'
		    f'{("Successful Orders: "+str(aivals["served"])).rjust(COL_WIDTH//2+3)}')
	print(left.ljust(COL_WIDTH) + ' | ' + right.ljust(COL_WIDTH))
	
	# Prints the total customers to serve and the quota for the round
	left = (f'{("Total Customers: "+str(vals["total"])).ljust((COL_WIDTH//2-3))}'
		    f'{("Quota for the round: "+str(quota)).rjust(COL_WIDTH//2+3)}')
	right = (f'{("Total Customers: "+str(aivals["total"])).ljust((COL_WIDTH//2))}'
		    f'{("Quota for the round: "+str(quota)).rjust(COL_WIDTH//2+3)}')
	print(left.ljust(COL_WIDTH) + ' | ' + right.ljust(COL_WIDTH))

	print_Border()															# Prints the border
	print_Header("[Trays]")													# Prints the [Trays] header
	print_Subtray("ABC")													# Prints the trays ABC
	print_Subtray("DEF")													# Prints the trays DEF	
	print_Header("[Counters]")												# Prints the [Trays] header
	print_Subcounter("ABC")													# Prints the counters
	remainingCounters = {'EASY': '', 'MEDIUM': 'D', 'HARD': 'DE'}[diffi]	# Checks which counters to print depending on the difficulty
	print_Subcounter(remainingCounters)										# Prints the remaining counter
	print_Border()

def game_Function(name,diffi,trays,counters):								#Function for the game
	COL_WIDTH =  int(shutil.get_terminal_size().columns // 2) - 3
	
	# Player records
	playerStreak = {"current": 0, "longest": 0}
	playerVals = {"count": 0, "total": 10, "rounds": 1, "served": 0, "score": 0}
	playerTotal = {"count": 0, "served": 0}
	
	# AI records
	aiStreak = {"current": 0, "longest": 0} 
	aiVals = {"count": 0, "total": 10, "rounds": 1, "served": 0, "score": 0}
	aiTotal = {"count": 0, "served": 0}

	# ingame variables
	multiplier = counter_Preparation(diffi,counters,aiCounters)				#Stores the final score multiplier and prepares
	proceed = 1 															#Indicator whether or whether you can proceed next round.
	while True:
		if proceed == 0:													#Ends the game when proceed is 0
			game_Over(name,diffi,playerTotal,playerVals,multiplier,playerStreak)				#Prints the players summary of journey
			break

		quota = Quota(diffi,playerVals)											#Stores the quota
		customers = generateCustomers(playerTotal["count"])
		aiMovePrompt = ""
		clear_Screen()

		while True:
			if playerVals["count"] == playerVals["total"] and counter_Empty(counters) == True and aiVals["count"] == aiVals["total"] and counter_Empty(aiCounters):			#If max count of customers, the round ends
				if playerVals["served"] < quota or playerVals["score"] < aiVals["score"]:														#Checks if customers served does reaches the quota
					clear_Screen()
					if playerVals["score"] < aiVals["score"]:
						prompt = "AI scored a higher score, better luck next time!" 
					else:
						prompt = "You failed to reach the required number of successful orders." 
					print(f"Level Failed!\n{prompt}")
					proceed = 0													#Sets the player elligible for next round
					empty_Tray(trays)											#Empties the tray
					empty_Tray(aiTrays)
					playerTotal["count"] += playerVals["count"]					#Records the total count of customers
					playerTotal["served"] += playerVals["served"]				#Records the total rounds
					placeholder = input("Press ENTER to continue.")
					break

				else:
					clear_Screen()
					print("Level Completed!\nPreparing the next level.")
					placeholder = input("Press ENTER to continue.")
					empty_Tray(trays)
					playerVals = {	"count": 0, 								#updates the Count, Total, Rounds, Served, and Score
				   					"total": playerVals["total"]+5,
									"rounds": playerVals["rounds"]+1,
									"served": 0,
									"score": playerVals["score"]
								}
					aiVals = {	"count": 0, 								#updates the Count, Total, Rounds, Served, and Score
				   					"total": playerVals["total"]+5,
									"rounds": playerVals["rounds"]+1,
									"served": 0,
									"score": playerVals["score"]
								}
					playerTotal["count"] += playerVals["count"]					#Records the total count of customers
					playerTotal["served"] += playerVals["served"]				#Records the total rounds
					break

			print_Display(name,diffi,playerVals,quota,playerStreak,aiVals,aiStreak)			#Prints the display
			
			Game_Menu(aiMovePrompt)																		#Prints the game menu

			if main_Action(trays,counters,playerVals,quota,playerStreak,diffi,name):		#Calls the function for the main function
				clear_Screen()
				continue
			aiMovePrompt = improvedAI.ai_decision(aiCounters, aiTrays, aiVals, quota, aiStreak)			#AI decision making | returns a prompt on what move the AI did
			
			increment_Tray(trays)															#Increments the tray
			increment_Tray(aiTrays)															#Increments the tray

			counter_System(counters,playerVals)												#Carries out the function for the system of counters
			counter_System(aiCounters,aiVals)												#Carries out the function for the system of counters

			input("\nPress ENTER to continue.")

			clear_Screen()

			userCustomerWalkedAwayPrompt = unsuccessful_Order(counters,playerStreak)								#Decrements each patience of the customer and return prompt if user walked away
			aiCustomerWalkedAwayPrompt = unsuccessful_Order(aiCounters,aiStreak)									#Decrements each patience of the customer and return prompt if user walked away
			if userCustomerWalkedAwayPrompt or aiCustomerWalkedAwayPrompt:
				print(userCustomerWalkedAwayPrompt.ljust(COL_WIDTH) + ' | ' + aiCustomerWalkedAwayPrompt.ljust(COL_WIDTH))

	final_score = playerVals["score"]*multiplier									#Multiplies score to the multiplier and stores in a variable
	return [final_score,name,playerVals["rounds"],diffi]							#returns the following in order: final score, name, rounds, difficulty

if __name__ == '__main__':
	pass