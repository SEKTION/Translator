#!/usr/bin/env python3
try:
	
	#Import necessary Modules
	
	from os import system
	from time import sleep
	import sys
	import subprocess as sp

	system('clear')

	#Defining Variables

	RED = sp.getoutput('tput setaf 9')
	GREEN = sp.getoutput('tput setaf 10')
	YELLOW = sp.getoutput('tput setaf 11')
	BLUE = sp.getoutput('tput setaf 4')
	CYAN = sp.getoutput('tput setaf 14')
	WHITE = sp.getoutput('tput setaf 15')

	#Check Internet Connectivity

	connection = system('ping -c 2 goo.gl > /dev/null 2>&1')
	if connection != 0:
		print(RED)
		sys.exit("Please check your Internet connection!\n")

	#Check necessary tools and install if not already installed
		
	check = system('mpg123 --version > /dev/null 2>&1')
	if check != 0:
		print(GREEN)
		print("Setting up... Please wait...", flush=True)
		system('chmod +x trans && sudo apt-get install mpg123 -y > /dev/null 2>&1')
		print("\nReady!\n")
	

	#Dictionary with language codes

	lang_list = {}
	with open('langs.txt','r') as file:
		lang_list = dict([line.split('-') for line in file])

	help = {
		'1 to 5':'Self Explanatory',
		'clear':'clear Screen',
		'quit/q':'exit',
		'help':'You are looking right at it baby!'
	}

	#Defining Functions

	def print_list():
		for i,j in enumerate(lang_list, start=1):
				print(YELLOW)
				print(str(i) + ' : ' + j, end="\n", flush=True)
				sleep(0.1)

	def translate():
		source = 'English'
		source = input("\nType the Source language [Default-English]: ").title()
		if source.strip() == '':
			source = 'English'
		target = input("\nType the target language: ").title()
		source = lang_list.get(source, 'Language Not Available!')
		target = lang_list.get(target, 'Language Not Available!')
		output = './trans -b -shell ' + source.strip() + ':' + target.strip()
		print(YELLOW)
		system(output)

	def identify():
		word = input("\nEnter a word or a sentence: ")
		output = './trans -identify -no-auto ' + "'" + word + "' | grep -i name"
		print(YELLOW)
		lang_id = sp.getoutput(output).split()
		print('\n' + lang_id[1] + '\n')

	def pronounce():
		print(BLUE)
		system('./trans -b -speak -shell')

	print('\n\t\t\t' + RED + 'Welcome to the Language Translator\n')
	print('\t\t\t' + GREEN + '[\tAuthor : SEKTION\t]')
	print('\t\t\t' + GREEN + '[\tVersion : 1.0\t\t]\n')
	
	#Main-Menu which will run in loop until exit

	while True:
		print('\t\t\t\t' + CYAN + 'Select an Option!\n')
		opts = ["List Available Languages","Translate words or sentences","Identify a language","Text-to-Speech","Help"]
		for i,opt in enumerate(opts, start=1):
			print(str(i) + ' : ' + opt)

		cmd = input("\n> ").strip()

		if cmd == '1':
			system('clear')
			print_list()
				
		elif cmd == '2':
			translate()
		elif cmd == '3':
			identify()
		elif cmd == '4':
			pronounce()
		elif cmd == '5' or cmd == 'help':
			for k,v in dict.items(help):
				print(WHITE) 
				print('\t\t\t' + k + '\t:\t' + v + '\n')
				
			q = ""
			print(CYAN)
			while q != 'b' or q == 'q':
				q = input("Type 'b' to go back: ").strip()
				if q == 'q':
					sys.exit("\nGoodbye!\n")
			
		elif cmd == 'clear':
			system('clear')
		elif cmd == 'quit' or cmd == 'q':
			sys.exit("\nGoodbye!\n")

#Catch Keyboard Interrupt

except KeyboardInterrupt:
	print("\n\nNo need to be abrupt! You can always type 'q' to quit :)\n")		