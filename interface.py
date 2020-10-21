from tkinter import *
from tkinter import scrolledtext
from library import funcs


class MyFirstGUI:
    def __init__(self, master):
        self.master = master


        self.begin_pointer = 0
        self.end_pointer = 0

                
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

        self.pointers = Label(master, text=f"begin={self.begin_pointer}     end={self.end_pointer}")
        self.pointers.grid(row=1, column=2)
        # Create a Tkinter variable
        self.selected_func = StringVar(self.master)

        # Dictionary with options
        self.choices = sorted([i for i in self.__dir__() if i.startswith("run_")])
        self.selected_func.set(self.choices[0]) # set the default option

        self.popupMenu = OptionMenu(self.master, self.selected_func, *self.choices)
        Label(self.master, text="Choose a command").grid(row = 2, column=0)
        self.popupMenu.grid(row = 2, column=1)

        # # on change dropdown value
        # def change_dropdown(*args):
        #     print( self.selected_func.get() )

        # link function to change dropdown
        # self.selected_func.trace('w', change_dropdown)

        Button(self.master, text="Run command", command=self.run_func).grid(row=2, column=2)
        Button(self.master, text="Save buffer", command=self.save_buffer).grid(row=4, column=0)
        
    def run_func(self):
        name = self.selected_func.get()
        
        getattr(self, name)()

        

        # self.buffer.configure(state="normal")
        # self.buffer.insert(END, "Hello")
        # self.buffer.configure(state="disabled")


    def save_buffer(self):
        print(self.buffer.get("1.0",END))

    def run(self):
        self.master.mainloop()

    def run_search_to_word(self):
        res = funcs[self.selected_func.get()](self.textarea.get("1.0",END))
        print(self.selected_func.get())

    def run_forward_word(self):
        res = funcs[self.selected_func.get()](self.textarea.get("1.0",END))
        print(self.selected_func.get())

    def run_delete_by_text(self):
        res = funcs[self.selected_func.get()](self.textarea.get("1.0",END))
        print(self.selected_func.get())

    def run_delete_by_pointers(self):
        res = funcs[self.selected_func.get()](self.textarea.get("1.0",END))
        print(self.selected_func.get())

    def run_add_at_begin(self):
        res = funcs[self.selected_func.get()](self.textarea.get("1.0",END))
        print(self.selected_func.get())

    def run_copy_to_buffer(self):
        res = funcs[self.selected_func.get()](self.textarea.get("1.0",END))
        print(self.selected_func.get())

    




'''
где курсор
длина текста

'''

MyFirstGUI(Tk()).run()