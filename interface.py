from tkinter import *
from tkinter import scrolledtext
from library import funcs


class MyFirstGUI:
    def __init__(self, master):
        self.master = master

        self.begin_pointer = IntVar(master)
        self.end_pointer = IntVar(master)
                
        self.begin_pointer.set(0)
        self.end_pointer.set(0)

        self.pointers_label = StringVar(master)
        self.pointers_label.set(f"begin={self.begin_pointer.get()}     end={self.end_pointer.get()}")

        self.begin_pointer.trace_add("write", self.update_label)
        self.end_pointer.trace_add("write", self.update_label)

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

        self.pointers = Label(master, textvariable=self.pointers_label)
        self.pointers.grid(row=1, column=2)
        # Create a Tkinter variable
        self.selected_func = StringVar(self.master)

        # Dictionary with options
        self.choices = sorted([i for i in self.__dir__() if i.startswith("run_")])
        self.selected_func.set(self.choices[0]) # set the default option

        self.popupMenu = OptionMenu(self.master, self.selected_func, *self.choices)
        Label(self.master, text="Choose a command").grid(row = 2, column=0)
        self.popupMenu.grid(row = 2, column=1)

        Button(self.master, text="Run command", command=self.do_command).grid(row=2, column=2)
        Button(self.master, text="Save buffer", command=self.save_buffer).grid(row=4, column=0)
        
    def update_label(self, *args):
        self.pointers_label.set(f"begin={self.begin_pointer.get()}     end={self.end_pointer.get()}")

    def do_command(self):
        name = self.selected_func.get()
        getattr(self, name)()

    def save_buffer(self):
        print(self.buffer.get("1.0",END))

    def run(self):
        self.master.mainloop()

    def set_textarea(self, value):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, value)

    def run_search_to_word(self):
        s = self.textarea.get("1.0",END)
        text = self.input_word.get()
        
        res = funcs[self.selected_func.get()](s, text)
        if res is None:
            print(self.selected_func.get(), "error")
            return
        
        self.begin_pointer.set(res[0])
        self.end_pointer.set(res[1])
        

    def run_forward_word(self):
        s = self.textarea.get("1.0",END)
        res = funcs[self.selected_func.get()](s, self.begin_pointer.get())
        if res is None:
            print(self.selected_func.get(), "error")
            return
        
        self.begin_pointer.set(res[0])
        self.end_pointer.set(res[1])

    def run_delete_by_text(self):
        s = self.textarea.get("1.0",END)
        text = self.input_word.get()
        res = funcs[self.selected_func.get()](s, text)
        if res is None:
            print(self.selected_func.get(), "error")
            return
        
        self.set_textarea(res)
        self.begin_pointer.set(0)
        self.end_pointer.set(0)

    def run_delete_by_pointers(self):
        s = self.textarea.get("1.0",END)
        res = funcs[self.selected_func.get()](s, self.begin_pointer.get(), self.end_pointer.get())
        if res is None:
            print(self.selected_func.get(), "error")
            return
        
        self.set_textarea(res)
        self.begin_pointer.set(0)
        self.end_pointer.set(0)

    def run_add_at_begin(self):
        s = self.textarea.get("1.0",END)
        text = self.input_word.get()
        res = funcs[self.selected_func.get()](s, self.begin_pointer.get(), text)
        if res is None:
            print(self.selected_func.get(), "error")
            return
        
        self.set_textarea(res[0])
        self.begin_pointer.set(res[1])
        
    def run_copy_to_buffer(self):
        s = self.textarea.get("1.0",END)
        res = funcs[self.selected_func.get()](s, self.begin_pointer.get(), self.end_pointer.get())
        
        if res is None:
            print(self.selected_func.get(), "error")
            return
        
        self.buffer.configure(state="normal")
        self.buffer.insert(END, res)
        self.buffer.configure(state="disabled")


MyFirstGUI(Tk()).run()