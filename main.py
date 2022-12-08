from tkinter import *
from PyDictionary import PyDictionary

# storing PyDictionary
dictionary = PyDictionary()

# making main window
root = Tk()
root.geometry("500x500")
root.title('Dictionary')
root.iconbitmap("./icon/icon.ico")

def get_meaning():
    value = inputElem.get()
    # print(dictionary.meaning(value)
    word = dictionary.meaning(value)
    print(word.values()[0])
    # Label(root, text=, font=('Arial', 18)).grid(row=3, column=0)

# welcome text
welcomeTextLb = Label(root, text='Welcome!!', font=('Arial', 18))

# word input
inputLb = Label(root, text='Enter any word:', font=('Arial', 18))
inputElem = Entry(root, font=('Arial', 18))


enterBtn = Button(root, text='Enter', font=('Arial', 18), command=get_meaning)

# showing in the window
welcomeTextLb.grid(row=0, column=1, padx=15)

inputLb.grid(row=1, column=0, padx=15)

inputElem.grid(row=1, column=1)

enterBtn.grid(row=2, column=1)


# running the window
root.mainloop()