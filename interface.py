from tkinter import *
from tkinter import scrolledtext
import library

window = Tk()


window.title("Text editor")
window.geometry("800x600")



textarea = scrolledtext.ScrolledText(window,width=99,height=20)
buffer = scrolledtext.ScrolledText(window,width=99,height=10, state=DISABLED).grid(row=3, column=0, columnspan=4)
input_word = Entry(window,width=30)
label_input_word = Label(window, text="Input word: ")

textarea.grid(row=0, column=0, columnspan=4)
label_input_word.grid(row=1, column=0)
input_word.grid(row=1, column=1)

# Create a Tkinter variable
tkvar = StringVar(window)

# Dictionary with options
choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}
tkvar.set('Pizza') # set the default option

popupMenu = OptionMenu(window, tkvar, *choices)
Label(window, text="Choose a command").grid(row = 2, column=0)
popupMenu.grid(row = 2, column=1)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)

Button(window, text="Run command").grid(row=2, column=2)
Button(window, text="Save buffer").grid(row=4, column=0)


'''
где курсор
длина текста

'''

window.mainloop()