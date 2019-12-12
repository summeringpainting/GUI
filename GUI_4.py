from tkinter import *
import random

guessRange = "guessRange"
root = Tk()

e = Entry(root)
e.pack(pady=20)
e.focus_set()

class coastButtons():
    def printtext(self):
        global e
        string = e.get()
        print(string)

    def __init__(self, master, counter=0, counter1=1, luckvar=3, countup=2, level=1):
        frame = Frame(master)
        frame.pack()

        luck = random.randint(1, luckvar)

        self.Label = Label(text="You are on LVL " + str(level) + "! To win EASY pick a number between 1 to " + str(luckvar) + " in " + str(countup) + " guesses", padx=20, pady=40)
        self.Label.pack(side=TOP, pady=40)

        self.printButton = Button(frame, text="OK", command=self.printtext)
        self.printButton.pack(side=LEFT)

        self.printButton = Button(frame, text="quit", command=frame.quit)
        self.printButton.pack(side=LEFT)



root.title("Guessing Game")
root.geometry("400x200")
#c = textInput(root)
b = coastButtons(root)
root.mainloop()
