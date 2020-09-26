try:
	from os import system
	import sys

	system('clear')

	connection = system('ping -c 2 goo.gl > /dev/null 2>&1')
	if connection != 0:
		sys.exit("Please check your Internet connection!")

	check = system('mpg123 --version > /dev/null 2>&1')
	if check != 0:
		print("Setting up... Please wait...", end="", flush=True)
		system('sudo apt-get install mpg123 -y > /dev/null 2>&1')
		print("\nReady!\n")

	lang_list = {}
	with open('langs.txt','r') as file:
		lang_list = dict([line.split('-') for line in file])

	def print_list():
		for i,j in enumerate(lang_list, start=1):
				system("echo '\e[1;34m'")
				print(str(i) + ' : ' + j, end="\n")

	def translate():
		target = input("\nType the target language: ").title()
		target = lang_list.get(target, 'Language Not Available!')
		word = input("\nEnter a word or a sentence to translate: ")
		output = './trans -b ' + "'" + word + "'" + ' -t ' + target
		system('echo "\e[1;34m"')
		system(output)
		system('echo "\e[1;0m"')

	def identify():
		word = input("\nEnter a word or a sentence: ")
		output = './trans -identify -no-auto ' + "'" + word + "' | head -n1"
		system('echo "\e[1;34m"')
		system(output)
		system('echo "\e[1;0m"')

	def pronounce():
		word = input("\nEnter a word or a sentence: ")
		output = './trans -speak -no-translate ' + "'" + word + "'"
		system('echo "\e[1;34m"')
		system(output)
		system('echo "\e[1;0m"')

	system("echo '\n\t\t\e[1;31mWelcome to the Language Translator - A Python Script\n'")
	system("echo '\t\t\t\e[1;32m[\tAuthor : SEKTION\t]'")
	system("echo '\t\t\t\e[1;32m[\tVersion : 1.0\t\t]'")
	
	while True:
		system("echo '\n\t\t\t\t\e[1;36mSelect an Option!\n'")
		opts = ["See list of Available Languages","Translate a word or a sentence","Identify a language","Listen to pronunciation","Help"]
		for i,opt in enumerate(opts, start=1):
			print(str(i) + ' : ' + opt)

		choice = input("\n> ").strip()

		if choice == '1':
			system('clear')
			print_list()
			system('read _')	
		elif choice == '2':
			translate()
		elif choice == '3':
			identify()
		elif choice == '4':
			pronounce()
		elif choice == '5' or choice == 'help':
			system("echo '\n\t\t\t1 to 5 : Self Explainatory\n\n\t\t\thelp : You are looking right at it baby!\n\n\t\t\tclear : clear Screen\n\n\t\t\tquit or q : exit\n\n'")
			q = input("Type 'b' to go back: ").strip()
			while q != 'b':
				#print("Uh-Oh! Wrong Choice!")
				q = input("Type 'b' to go back: ").strip()  
			
		elif choice == 'clear':
			system('clear')
		elif choice == 'quit' or choice == 'q':
			sys.exit("\nGoodbye!")


except KeyboardInterrupt:
	print("\nNo need to be abrupt! You can always type 'q' to quit :)")		