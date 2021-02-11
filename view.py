import tkinter as tk
from tkinter import ttk
import tkinter.filedialog as fd

class View(tk.Tk):
    BUTTON_CAPTIONS = ['Select', 'Com', 'Flash']
    def __init__(self,controller):
        super().__init__()
        self.controller=controller
        self.filePath=""
        self.serialSelected =""
        self.colors = ("Purple", "Yellow", "Red", "Blue")
        self.label_Comselect = ttk.Label(self, text="Select COM")
        self.label_Comselect.grid(row=0, column=0, sticky="w")
        self.label_fileselect = ttk.Label(self, text="Select File")
        self.label_fileselect.grid(row=1, column=0, sticky="w")
        self.entryVar = tk.StringVar()
        self.ent = tk.Entry(self, textvariable=self.entryVar)
        self.ent.grid(row=1, column=1, sticky="nsew")
        self.combo = ttk.Combobox(self, values=self.controller.grabValues(),width=50)
        self.combo.bind("<<ComboboxSelected>>", self.callback)
        # self.combo.bind("<<ComboboxSelected>>", lambda button=self.selected_month.get(): self.controller.on_button_click(button))
        self.combo.grid(row=0, column=1, sticky="e")
        self.btn_file = ttk.Button(self, text="Browse", command=self.choose_file)
        self.btn_file.grid(row=1, column=3, sticky="e")
        self.btn_flash= ttk.Button(self, text="Flash",
                                   command=(lambda button="flash": self.controller.on_button_click(button)))
        self.btn_flash.grid(row=4, column=3, sticky="e")


        #self.make_buttons()

    def main(self):
        print("In main of view")
        self.geometry("680x300")
        self.mainloop()

    def callback(self, *args):
        selection = self.combo.get()
        print("Your selection is", selection)
        self.serialSelected=self.combo.get()
        self.controller.on_button_click("comSelected")


    def choose_file(self):
        filetypes = (("Plain text files", "*.txt"),("hex files", "*.hex"),("All files", "*"))
        filename = fd.askopenfilename(title="Open file",initialdir="/", filetypes=filetypes)
        if filename:
            self.entryVar.set(filename)
            self.filePath=filename
            print("In vview filepath set to ",self.filePath)
            self.controller.on_button_click("fileSelected")

            return filename
        else:
            return 0

if __name__ == '__main__':
    pass