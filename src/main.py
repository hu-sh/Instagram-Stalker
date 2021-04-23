from Instabot import Instabot
from Menu import Menu

import configparser
import os.path


def readFromFile(nick, sel):
	f = open(sel+"/"+nick+'.txt', 'r')
	names=[]
	for line in f:
		names.append(line[0:-1])
	f.close()
	return names


def writeToFile(names, nick, sel):
	f = open(sel+"/"+nick+".txt", 'w')

	for name in names:
		f.write(name+'\n')
	f.close()


def cerca(nick, sel):
	return os.path.exists(sel+"/"+nick+'.txt')


def compara(liste, salvati):
	combaciati = {}
	combaciatori = []

	i = 0

	for name in salvati:
		
		i+=1
		
		for persona in liste[name]:
			
			counter = 1
			#trovato = False

			#for j in combaciatori:
			#	if not trovato:
			#		if name in combaciati[j]:
			#			trovato = True;
			#	else:
			#		break

			#if not trovato:
			for n in range(i, len(salvati)):
					
				if persona in liste[salvati[n]] : #and persona not in combaciati
						
					counter += 1
						
					try:
						combaciati[counter].append(persona)
					except KeyError:
						combaciati[counter]=[]
						combaciati[counter].append(persona)
						
					if counter not in combaciatori:
						combaciatori.append(counter)



	return combaciati, combaciatori


if __name__ == "__main__":
	
	parser = configparser.ConfigParser()

	parser.read("../file/config.ini")
	
	username = parser["Account"]["username"]
	password = parser["Account"]["password"]

	if username == "" or password == "":
		username = parser["Account"]["username"] = input("Insert the username: ")
		password = parser["Account"]["password"] = input("Insert the password: ")
		parser.write("../file/config.ini")


	os.system("clear")

	liste = {}
	salvati = []
	sel = 0
	nick = ""
	menu = Menu("INSTA-Stalker", [	"Search an account",
							  	   	"Compare saved accounts",
						      		"Clear the account list",
									"Change the owner account"
							  	])

	created = False

	
	menu.show()
	menu.setChoice()

	while  not menu.esc():

		if menu.getChoice()==1:
			os.system("clear")

			nick = input("Account: ")
			
			sel=0

			while sel != 1 and sel != 2:
				sel = int(input("Followers / Following: "))


			if sel==1:
				found = cerca(nick, "followers")

			elif sel==2:
				found = cerca(nick, "following")


			if not get:
				get = int(input("File not found.\
									  \nContinue to execute? (1 yes, 2 no)? "))
			else:
				get = int(input("File found.\
									  \nUpdate / Continue / Save (1, 2, 3) : "))
			

			if get==1:
				if not created:
					bot = Instabot(username, password)


				if sel==2:
					try:
						writeToFile(bot.get_following(nick), nick, "following")
					except Exception:
						print(Exception)

				elif sel==1: 
					#try:
					writeToFile(bot.get_followers(nick), nick, "followers")
					#except Exception:
						#print(Exception)


			elif get==3:

				if sel==1:
					liste[nick]=readFromFile(nick, "followers")
				elif sel==2:
					liste[nick]=readFromFile(nick, "following")
					salvati.append(nick)

				print("\nFile saved!\n")


		elif menu.getChoice() == 2:
			combaciati, combaciatori = compara(liste, salvati)
			
			os.system("clear")

			print ("Here we are all the account that match with followers and followings:\n"+combaciati)


		elif menu.getChoice() == 3:
			liste = {}
			salvati = []
			combaciati = {}
			combaciatori = []

			os.system("clear")
			print("I cleared it all!\n")

		elif menu.getChoice() == 4:
			username = parser["Account"]["username"] = input("Insert the username: ")
			password = parser["Account"]["password"] = input("Insert the password: ")
			parser.write("../file/config.ini")

		menu.show()
		menu.setChoice()
	
	
