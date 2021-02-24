from pyautogui import click, press, keyDown, keyUp, tripleClick, rightClick
from tkinter import Tk, Button, Entry, Label
from time import sleep

def startClick(atc, delayCount):
	if len(delayCount) > 0:
		click(x=200, y=200)
		IATC = int(atc)
		sleep(int(delayCount))
		for i in range(IATC):
			tripleClick()
	else:
		pass


def startBridge(atB, delayCount):
	if len(delayCount) > 0:
		click(x=200, y=200)
		atbLoop = int(atB)
		sleep(int(delayCount))
		for j in range(atbLoop):
			rightClick()
			rightClick()
			rightClick()
	else:
		pass


def main():
	maw = Tk()
	maw.title("Autoclicker")
	# autoclicker

	Label(maw, text="Attack", font=150).pack()
	Label(maw, text="Enter the autoclick delay amount:").pack()
	autoDelay = Entry()
	autoDelay.pack()
	Label(maw, text="Enter the amount to autoclick:").pack()
	autoClickAmount = Entry(maw)
	autoClickAmount.pack()
	Button(maw, text="Start autocliker", command=lambda: startClick(autoClickAmount.get(), autoDelay.get())).pack()
	Label(maw, text="___________________________________________", font=150).pack()
	
	# auto line builder
	Label(maw, text="Builder", font=150).pack()
	Label(maw, text="Enter the build delay amount: ").pack()
	buildDelay = Entry(maw)
	buildDelay.pack()
	Label(maw, text="Enter the build clicks amunt: ").pack()
	autoBuildAmount = Entry(maw)
	autoBuildAmount.pack()
	Button(maw, text="Start autonormal builder", command=lambda: startBridge(autoBuildAmount.get(), buildDelay.get())).pack()
	Label(maw, text="___________________________________________", font=150).pack()

	
	# running the gui loop
	maw.mainloop()
main()
