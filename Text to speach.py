import os
import pyttsx3 as ts


ts.speak("Hey user what can I do for you?")
while True:
	print("Hey user what can I do for you : ",end='')
	p=input("")
	p=p.lower()
	if ("open" in p) or ("execute" in p) or ("find" in p) or ("run" in p):
			if ("firefox" in p):
				os.system("firefox")
			elif ("editor" in p) or ("notepad" in p) or ("gedit" in p):
				os.system("notepad")
			elif ("video" in p) or ("vlc" in p):
				os.system("vlc")
			elif ("writer" in p) or ("word" in p):
				os.system("libreoffice --writer")
			elif ("draw" in p) or ("paint" in p):
				os.system("libreoffice --draw")
			elif ("impress" in p) or ("powerpoint" in p):
				os.system("libreoffice --impress")
			elif ("calc" in p) or ("excel" in p):
				os.system("libreoffice --calc")
			elif ("code" in p) or ("code." in p):
				os.system("anaconda")
			elif ("GIthub" in p) or ("git" in p):
				os.system("GIthub Desktop")
			elif ("html" in p):
				os.system("libreoffice --web")
			else:
				ch=input("Sorry,I don't understand that. Should I search it on internet [y/n]: ")
				if ch=="y":
					os.system("firefox "+p)
				else:
					break
			elif ("visit" in p):
				os.system("firefox "+p[5:])
		       elif ("done" in p) or ("quit" in p) or ("exit" in p):
			print("See you soon, Take care.")
			break
		      elif ("install" in p) or ("download" in p):
			os.system("sudo apt install gimp")
	else:
		ch=input("Sorry [y/n]: ")
		if ch=="y":
			os.system("firefox "+p)
ts.speak("See  you  soon   , take   care.")
	
