import serial
import numpy as np 
import matplotlib.pyplot as plt
import tkinter
import os

arduino = serial.Serial("/dev/cu.usbmodem14101", timeout=1)
ready = 0

def commencer():
	rawdata= []
	global ready
	for k in range(0, 10, 1):
		print("Chargement {}".format("*"*k))
		rawdata.append(arduino.readline()[:-2])
		os.system("clear")

	with open("data.txt", "w") as files:
		for k in rawdata:
			files.write(k.decode("utf-8") + "\n")

	arduino.write(b'1')
	ready = 1
	message2["text"]= "Mesure prise"
	return

def afficher():
	global ready
	if ready:
		vals, temps = np.loadtxt("data.txt", delimiter = ';', unpack = True)
		plt.plot(temps, vals)
		plt.show()
		arduino.write(b'0')
		message2["text"]= "Mesures Supprimer"
	else:
		print("Aucune mesure prise")
	ready = 0
	return

fenetre = tkinter.Tk()

button = tkinter.Button(fenetre, text="Prendre des mesures", command = commencer)
button2 = tkinter.Button(fenetre, text="Afficher le graphe des mesures", command = afficher)
message = tkinter.Label(fenetre, text="Bienvenue dans l'interface graphique \n pour prendre des mesure !!")
message2 = tkinter.Label(fenetre, text="Aucune mesure prise pour l'instant")


message.pack()
button.pack()
message2.pack()
button2.pack()

fenetre.mainloop()
