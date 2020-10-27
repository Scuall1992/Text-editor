from tkinter import *
from tkinter import scrolledtext, filedialog
from library import funcs
import os
from sys import platform

v_lesu = '''В осеннем лесу
Я рад предстоящей встрече с осенним лесом. Иду как в картинную галерею еще раз взглянуть на знакомые полотна, что ежегодно выставляет напоказ золотая осень. Глаз насторожен и жаден: не хочется ничего упустить.
У самого края леса,в зарослях,  блеснуло озеро с темной водой цвета крепкого заваренного чая. На его поверхности цветная мозаика из листьев, занесенных ветром. У берега горбится старая сеть, брошенная за ненадобностью. Это Поленов.
Обычай, дошедший из глубин веков, от языческого суеверия.
Я тоже медленно снимаю шапку, но не как язычник, Я вхожу под своды леса как в залы неповторимого шишкинского гения.
Мы идем мимо развешанных полотен но пестротканой лесной дорожке. Она то желтеет лимонными листьями берез, то розовеет осыпью кустарника, то окрашивается в оранжевое и багровое, когда пробираемся под осинами. Узорчатые листья рябины стали пунцово- красными, и в тон им, только еще ярче, пламенеют тяжелые кисги ягод. Тропинка ведет еще дальше и дальше, глаза начинают уставать от ярких красок, а этому беспечному расточительству по-прежнему нет конца.'''


class MyFirstGUI:
    def __init__(self, master):
        self.master = master

        self.begin_pointer = IntVar(master)
        self.end_pointer = IntVar(master)

        self.begin_pointer.set(0)
        self.end_pointer.set(0)

        self.pointers_label = StringVar(master)
        self.pointers_label.set(
            f"begin={self.begin_pointer.get()}     end={self.end_pointer.get()}")

        self.begin_pointer.trace_add("write", self.update_label)
        self.end_pointer.trace_add("write", self.update_label)

        self.master.title("Text editor")
        self.master.geometry("800x650")

        self.textarea = scrolledtext.ScrolledText(
            self.master, width=99, height=20)
        self.buffer = scrolledtext.ScrolledText(
            self.master, width=99, height=10, state=DISABLED)

        self.buffer.grid(row=3, column=0, columnspan=4)
        self.input_word = Entry(self.master, width=30)
        self.label_input_word = Label(self.master, text="Input word: ")

        self.textarea.grid(row=0, column=0, columnspan=4)
        self.label_input_word.grid(row=1, column=0)
        self.input_word.grid(row=1, column=1)

        self.pointers = Label(master, textvariable=self.pointers_label)
        self.pointers.grid(row=1, column=2)

        self.status_var  = StringVar(self.master)
        self.status_var.set("Status line")
        self.status_line = Label(master, textvariable=self.status_var)
        self.status_line.grid(row=6, column=0)

        self.selected_func = StringVar(self.master)

        # Dictionary with options
        self.choices = sorted(
            [i for i in self.__dir__() if i.startswith("run_")])
        self.selected_func.set(self.choices[-1])  # set the default option

        self.popupMenu = OptionMenu(
            self.master, self.selected_func, *self.choices)
        Label(self.master, text="Choose a command").grid(row=2, column=0)
        self.popupMenu.grid(row=2, column=1)

        Button(self.master, text="Run command",
               command=self.do_command).grid(row=2, column=2)
        Button(self.master, text="Save buffer",
               command=self.save_buffer).grid(row=4, column=0)

        self.set_textarea(v_lesu)
        self.input_word.insert(0, "Поленов")
        self.run_search_to_word()
        self.input_word.delete(0, END)
        self.input_word.insert(0, "hello")

    def update_label(self, *args):
        self.pointers_label.set(
            f"begin={self.begin_pointer.get()}     end={self.end_pointer.get()}")

    def do_command(self):
        name = self.selected_func.get()
        getattr(self, name)()

    def get_path_to_desktop(self):
        if platform == "windows":
            return f"C:\\Users\\{os.getlogin()}\\Desktop"
        else:
            return f"~/Desktop/"

    def file_save(self, text2save):
        f = filedialog.asksaveasfile(initialdir = self.get_path_to_desktop(),title = "Select file",filetypes = [("txt files","*.txt")], mode="w")
        if f is None:
            return
        f.write(text2save)
        f.close()

    def save_buffer(self):
        s = self.buffer.get("1.0", END).strip()
        if len(s) > 0:
            self.file_save(s)
        else:
            self.status_var.set("Empty buffer. Nothing to save")

    def run(self):
        self.master.mainloop()

    def set_textarea(self, value):
        self.textarea.delete(1.0, END)
        self.textarea.insert(END, value)

    def run_search_to_word(self):
        s = self.textarea.get("1.0", END)
        text = self.input_word.get()

        res = funcs[self.selected_func.get()](s, text)
        if res is None:
            self.status_var.set(f"{self.selected_func.get()} error")
            return

        self.begin_pointer.set(res[0])
        self.end_pointer.set(res[1])
        self.status_var.set(f"{self.selected_func.get()} ok")

    def run_forward_word(self):
        s = self.textarea.get("1.0", END)
        res = funcs[self.selected_func.get()](s, self.begin_pointer.get())
        if res is None:
            self.status_var.set(self.selected_func.get())
            return

        if res != -1:
            self.begin_pointer.set(res[0])
            self.end_pointer.set(res[1])
            self.status_var.set(f"{self.selected_func.get()} ok")

    def run_backward_word(self):
        s = self.textarea.get("1.0", END)
        res = funcs[self.selected_func.get()](s, self.begin_pointer.get())
        if res is None:
            self.status_var.set(self.selected_func.get())
            return

        if res != -1:
            self.begin_pointer.set(res[0])
            self.end_pointer.set(res[1])
            self.status_var.set(f"{self.selected_func.get()} ok")

    def run_delete_by_text(self):
        s = self.textarea.get("1.0", END)
        text = self.input_word.get()
        res = funcs[self.selected_func.get()](s, text)
        if res is None:
            self.status_var.set(self.selected_func.get())
            return

        self.set_textarea(res)
        self.begin_pointer.set(0)
        self.end_pointer.set(0)
        self.status_var.set(f"{self.selected_func.get()} ok")

    def run_delete_by_pointers(self):
        s = self.textarea.get("1.0", END)
        res = funcs[self.selected_func.get()](
            s, self.begin_pointer.get(), self.end_pointer.get())
        if res is None:
            self.status_var.set(self.selected_func.get())
            return

        self.set_textarea(res)
        self.begin_pointer.set(0)
        self.end_pointer.set(0)
        self.status_var.set(f"{self.selected_func.get()} ok")

    def run_add_before(self):
        s = self.textarea.get("1.0", END)
        text = self.input_word.get()
        res = funcs[self.selected_func.get()](
            s, self.begin_pointer.get(), text)
        if res is None:
            self.status_var.set(self.selected_func.get())
            return

        self.set_textarea(res[0])
        self.begin_pointer.set(res[1])
        self.status_var.set(f"{self.selected_func.get()} ok")

    def run_add_after(self):
        s = self.textarea.get("1.0", END)
        text = self.input_word.get()
        res = funcs[self.selected_func.get()](
            s, self.begin_pointer.get(), text)
        if res is None:
            self.status_var.set(self.selected_func.get())
            return

        self.set_textarea(res[0])
        self.begin_pointer.set(res[1])
        self.status_var.set(f"{self.selected_func.get()} ok")

    def run_copy_to_buffer(self):
        s = self.textarea.get("1.0", END)
        res = funcs[self.selected_func.get()](
            s, self.begin_pointer.get(), self.end_pointer.get())

        if res is None:
            self.status_var.set(self.selected_func.get())
            return

        if len(self.buffer.get(1.0, END)) == 0:
            res = res.strip()#TODO

        self.buffer.configure(state="normal")
        self.buffer.insert(END, res)
        self.buffer.configure(state="disabled")
        self.status_var.set(f"{self.selected_func.get()} ok")

MyFirstGUI(Tk()).run()
