import config, requests, json
from requests.auth import HTTPBasicAuth
s = config.sign('https://api.freelancehunt.com/skills', 'GET')
allcats = json.loads(requests.get('https://api.freelancehunt.com/skills', auth=HTTPBasicAuth(config.token, s)).text)
for i in allcats:
	print("["+i['skill_id']+"] "+i['skill_name'])
scats = input("Write categories in this format: '24,142,12' without literals and spaces: ")
f = open('cats', 'a')
f.write(scats)
f.close()