# Alexander Jobling

from urllib.request import urlopen
from xml.etree.ElementTree import parse
import ssl

ps3_server = 'https://a0.ww.np.dl.playstation.net/tpl/np/<GAMEID>/<GAMEID>-ver.xml'
context = ssl._create_unverified_context()

def get_game_update_info(gameid):

	game_update_info = {
		'Title': None,
		'Packages': []
	}

	update_address = ps3_server.replace('<GAMEID>', gameid)
	# there is a chance that a valid gameid will not be on the server causing
	# url_open to throw a HTTPError exception like BLJM55029
	update_request = urlopen(update_address, context=context) 
	update_xml = parse(update_request)

	title_xml = update_xml.iter('TITLE')
	title = next(title_xml)
	game_update_info['Title'] = title.text

	for package_xml in update_xml.iter('package'):
		version = package_xml.attrib.get('version')
		size = package_xml.attrib.get('size')
		url = package_xml.attrib.get('url')

		package_info = {
			'Version': version,
			'Size': str(round(int(size)/1024/1024, 2)) + "MiB",
			'Url': url
		}
		game_update_info['Packages'].append(package_info)
	
	return game_update_info

#print(get_game_update_info('BLUS30145'))
#print(get_game_update_info('NPUB30181'))
#print(get_game_update_info('BLES00760'))
