import requests
import argparse
from urllib.parse import urlparse

def argParserCommands():

	parser = argparse.ArgumentParser()
	parser.add_argument('-u','--url', dest="urlXss", help='Você deve setar a url a ser testada: Ex: https://example.com/?algo=', required=True)
	parser.add_argument('-ul','--login-url' , dest="loginUrl", help='Se o site precisa de login use esta variável', default=False)
	parser.add_argument('-d','--data', dest="postData", help='Data para iniciar a sessão no website.', default=False)

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

	if returnCommands.loginUrl != False:
		


	#loadFileGenerateList('xss_payloads.txt')