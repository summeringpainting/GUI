from tkinter import *

guessRange = "guessRange"
root = Tk()

e = Entry(root)
e.pack(pady=20)
e.focus_set()

class coastButtons:
    def printtext(self):
        global e
        string = e.get()
        print(string)

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.Label = Label(text="Guess a number from one to " + guessRange, padx=20, pady=40)
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
