#!/usr/bin/env python3

import pywinrm
from getpass import getpass

def main():
	print("WinRM Shell for Pen Testers")
	host = input("Host: ")
	user = input("Username: ")
	password =  getpass()
	try:
		s = winrm.Session(host, auth=(user,password))
	except:
		print("Incorrect login and/or host")
	try:
		while(True):
			cmd = input("#> ")
			splitInput = cmd.split(" ")
			s.run_cmd(splitInput[0], splitInput[1:])
	except KeyboardInterupt:
		print("You quit. Bye!")

if __name__ == "__main__":
	main()
