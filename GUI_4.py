from tkinter import *
import random
guessRange = "guessRange"
root = Tk()

e = Entry(root)
e.pack(pady=20)
e.focus_set()

class coastButtons():
    def printtext(self, counter=0, counter1=1, luckvar=3, countup=2, level=1):
        global e
        string = e.get
        string = int(e.get())
        loto = string
        luck = random.randint(1, luckvar)
        while luck != loto:

            if loto <= (luck + 3) and loto >= (luck - 3):
                counter += 1
                if counter > counter1:
                    print("too many guesses")
                    break
                else:
                    print("closey")
                    print(counter)
                    loto = string
            else:
                counter += 1
                if counter > counter1:
                    print("too many guesses")
                    break
                else:
                    print("Not closey")
                    loto = string
        else:
            print("WINWINWINWIN")


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
