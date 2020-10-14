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
			elif ("html" in p):
				os.system("libreoffice --web")
			else:
				ch=input("Sorry,I don't understand that. Should I search it on internet [y/n]: ")
				if ch=="y":
					os.system("firefox "+p)
				else:
					break
	