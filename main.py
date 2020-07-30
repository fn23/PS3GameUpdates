# Alexander Jobling

from gameid import is_game_id_structure_valid
from updateinfo import get_game_update_info

def print_info(gameupdateinfo):
	print('Title: ', gameupdateinfo['Title'])
	print('Update Packages: ', len(gameupdateinfo['Packages']))
	for package in gameupdateinfo['Packages']:
		print('Version: ', package['Version'])
		print('Size: ', package['Size'])
		print('Url: ', package['Url'])

def main():
	while True:
		gameid = input("PS3 GameID> ").upper().replace('-', '')
		if is_game_id_structure_valid(gameid):
			updateinfo = get_game_update_info(gameid)
		else:
			print('Invalid GameID Structure.')
			continue
		print_info(updateinfo)
		break

try:
	main()
except Exception as ex:
	print('Exception raised: ', ex)
