# Alexander Jobling

def check_digital_game_id(GameID):
	region_code = ['A', 'E', 'H', 'J', 'K', 'U']
	if GameID[0] in region_code:
		if GameID[1].isalpha():
			if GameID[2:].isnumeric():
				return True
	return False

def check_physical_game_id(GameID):
	rights_code = ['C', 'L']
	region_code = ['A', 'C', 'E', 'H', 'J', 'K', 'U']
	type_code = ['B', 'C', 'D', 'M', 'S', 'T', 'V', 'X', 'Z']
	if GameID[0] in rights_code:
		if GameID[1] in region_code:
			if GameID[2] in type_code:
				if GameID[3:].isnumeric():
					return True
	return False

def is_game_id_structure_valid(GameID):
	if len(GameID) == 9:
		if GameID.startswith("B"):
			return check_physical_game_id(GameID[1:])
		elif GameID.startswith("NP"):
			return check_digital_game_id(GameID[2:])
	return False

#test_id1 = "BLUS30145" # Physical
#test_id2 = "NPUB30181" # Digital
#test_id3 = "NPBLA4231" # Invalid ID
#print(is_game_id_structure_valid(test_id1))
#print(is_game_id_structure_valid(test_id2))
#print(is_game_id_structure_valid(test_id3))