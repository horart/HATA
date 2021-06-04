from colorama import init, Fore, Back, Style
init()
print(Fore.RED)
print('''

		 ▄         ▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄  ▄▄▄▄▄▄▄▄▄▄▄ 
		▐░▌       ▐░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌
		▐░▌       ▐░▌▐░█▀▀▀▀▀▀▀█░▌ ▀▀▀▀█░█▀▀▀▀ ▐░█▀▀▀▀▀▀▀█░▌
		▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌
		▐░█▄▄▄▄▄▄▄█░▌▐░█▄▄▄▄▄▄▄█░▌     ▐░▌     ▐░█▄▄▄▄▄▄▄█░▌
		▐░░░░░░░░░░░▌▐░░░░░░░░░░░▌     ▐░▌     ▐░░░░░░░░░░░▌
		▐░█▀▀▀▀▀▀▀█░▌▐░█▀▀▀▀▀▀▀█░▌     ▐░▌     ▐░█▀▀▀▀▀▀▀█░▌
		▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌
		▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌
		▐░▌       ▐░▌▐░▌       ▐░▌     ▐░▌     ▐░▌       ▐░▌
		 ▀         ▀  ▀         ▀       ▀       ▀         ▀                                                  
''')
print(Style.RESET_ALL)
import requests, json
url = 'https://api.freelancehunt.com/v2/projects?filter[only_my_skills]=1'
logdata = open('logdata').read().split("\n")[1]
projects = json.loads(requests.get(url, headers={'Authorization': "Bearer " + logdata}).text)
projects = sorted(projects['data'], key=lambda d: int(d['attributes']['bid_count']))
for i in projects:
	hasEnd = False
	while not hasEnd:
		ix = i['attributes']
		print(Fore.BLUE +  ix['status']['name'])
		print(ix['name'] + Style.RESET_ALL)
		print(ix['description'])
		q = ""
		for j in ix['skills']: q+=j['name'] + " "
		print(Fore.GREEN + "Skills: " + q)
		print("Bids: " + str(ix['bid_count']) + Style.RESET_ALL)
		a = input("Continue, break, bids, make a bid [c/ctrl+Z/v/x]?")
		if a == 'br':
			break
		elif a == 'v':
			burl = 'https://api.freelancehunt.com/v2/projects/' + str(i['id']) + "/bids"
			bids = json.loads(requests.get(burl, headers={'Authorization': "Bearer " + logdata}).text)['data']
			for k in bids:
				k = k['attributes']
				print(Back.RED)
				print(Fore.YELLOW)
				if k['is_hidden'] == False:
					print(k['comment'] + " : " + str(k['budget']['amount']) + k['budget']['currency'] + "\n\n")
				print(Style.RESET_ALL)
		elif a == 'i': print(i)
		elif a == 'x':
			days = int(input('How long? '))
			bud = {'amount': int(input('How much? ')), 'currency': curr}
			safe = input('Who pays for a safe? [employer/developer/split/n]')
			safe = safe if safe != n else '\\null'
			comm = input('Commentary: ')
			hid = bool(input('Leave empty if it\'s public: '))
			data = json.dumps({'days': days, 'budget': bud, 'safe_type': safe, 'comment': comm, 'is_hidden': hid}).replace("'\\null'", 'null')
			headers = {
  				'Authorization': 'Bearer ' + logdata,
  				'Content-Type': 'application/json'
			}
			response = requests.request("POST", i['links']['self']['api'] + '/bids', headers=headers, data=data)
		elif a == 'c':
			hasEnd = True
			continue
	print('\n\n\n\n')
print(Fore.GREEN + 'Goodbye!' + Style.RESET_ALL)