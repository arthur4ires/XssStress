import requests
import argparse
import re

def argParserCommands():

	parser = argparse.ArgumentParser()
	parser.add_argument('-u','--url', dest="urlXss", help='Você deve setar a url a ser testada: Ex: https://example.com/?algo=', required=True)
	parser.add_argument('-ul','--login-url' , dest="loginUrl", help='Se o site precisa de login use esta variável', default=False)
	parser.add_argument('-vs','--verify-session', dest="verifySession", help='Verificar sessão',default=False)
	parser.add_argument('-d','--data', dest="postData", help='Data para iniciar a sessão no website.', default=False)
	parser.add_argument('-ct','--csrf-token', dest="csrfToken", help='Puxar o valor da url de login.', default=False)

	return parser.parse_args()

def loadFileGenerateList(fileName):

	a = open(fileName, 'r')
	payloadsList = []

	for b, c in enumerate(a):
		payloadsList.append(c.replace('\n',''))

	return payloadsList

if "__main__" == __name__:
	
	returnCommands = argParserCommands()
	sessionBrowser =  requests.Session()

	if returnCommands.loginUrl != False and returnCommands.postData != False:
		
		dictLogin = {'':''}

		if returnCommands.csrfToken != False:

			htmlCsrf = sessionBrowser.get(returnCommands.loginUrl)

			regexValue = r'\$\("#' + returnCommands.csrfToken + '"\)\.val\(\'(.*)\'\);'

			csrfToken =  re.findall(regexValue, htmlCsrf.text);

			dictLogin[returnCommands.csrfToken] = csrfToken[0]

		postData = returnCommands.postData.split('&')

		for a in postData:

			dictLogin[a.split('=')[0]] = a.split('=')[1]

		sessionBrowser.post(returnCommands.loginUrl,data=dictLogin)

		if 'logado_true' in sessionBrowser.get(returnCommands.verifySession).text:
			print("[+] Usuário Logado")

	payloadsList = loadFileGenerateList('xss_payloads.txt')

	for a in payloadsList:

		urlXss = returnCommands.urlXss + '">' +  a
		htmlResponse = sessionBrowser.get(urlXss)

		if 'removed' in htmlResponse.text:
			print('[+] OK: {} - {}'.format(urlXss, a))
		else:
			print('[+] Averiguar: {} - {}'.format(urlXss, a))