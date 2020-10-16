from tkinter import *
from tkinter import scrolledtext
import library


class MyFirstGUI:
    def __init__(self, master):
        self.master = master
                
        self.master.title("Text editor")
        self.master.geometry("800x600")

        self.textarea = scrolledtext.ScrolledText(self.master,width=99,height=20)
        self.buffer = scrolledtext.ScrolledText(self.master,width=99,height=10, state=DISABLED)
        
        self.buffer.grid(row=3, column=0, columnspan=4)
        self.input_word = Entry(self.master,width=30)
        self.label_input_word = Label(self.master, text="Input word: ")

        self.textarea.grid(row=0, column=0, columnspan=4)
        self.label_input_word.grid(row=1, column=0)
        self.input_word.grid(row=1, column=1)

        # Create a Tkinter variable
        self.tkvar = StringVar(self.master)

        # Dictionary with options
        self.choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}
        self.tkvar.set('Pizza') # set the default option

        self.popupMenu = OptionMenu(self.master, self.tkvar, *self.choices)
        Label(self.master, text="Choose a command").grid(row = 2, column=0)
        self.popupMenu.grid(row = 2, column=1)

        # on change dropdown value
        def change_dropdown(*args):
            print( self.tkvar.get() )

        # link function to change dropdown
        self.tkvar.trace('w', change_dropdown)

        Button(self.master, text="Run command", command=self.insert_text).grid(row=2, column=2)
        Button(self.master, text="Save buffer", command=self.save_buffer).grid(row=4, column=0)
        
    def insert_text(self):
        print("insert")
        self.buffer.configure(state="normal")
        self.buffer.insert(END, "Hello")
        self.buffer.configure(state="disabled")


    def save_buffer(self):
        print(self.buffer.get("1.0",END))

    def run(self):
        self.master.mainloop()





'''
где курсор
длина текста

'''

MyFirstGUI(Tk()).run()