# Importing Required Module
import os
from tkinter import *
from tkinter import messagebox as ms
from tkinter import filedialog as fd
from tkinter import colorchooser

class main:
    def __init__(self,master):
        self.master = master
        self.header()
        self.widget()

    def header(self):
        self.master.title("Text Editor By C5")
        # Insert your application icon
        # self.master.iconbitmap("icon.ico")
        self.master.geometry("500x500+400+50")
        self.master.minsize(500,500)

    def newFile(self,event=None):
        self.file = None
        self.master.title("Untitle - C5")
        self.TextArea.delete(1.0,END)

    def openFile(self,event=None):
        self.file = fd.askopenfilename(defaultextension="txt",filetypes=[("Text File","*.txt"),("All Files","*.*")])
        if self.file == "":
            self.file = None
        else:
            self.master.title(os.path.basename(self.file))
            self.TextArea.delete(1.0,END)
            self.f = open(self.file,"r")
            self.TextArea.insert(1.0,self.f.read())
            self.f.close()

    def saveFile(self,event=None):
        if self.file == None:
            self.file = fd.asksaveasfilename(initialfile="newFile",defaultextension="txt",filetype=[("All Files","*.*")])
            if self.file:
                self.master.title(os.path.basename(self.file)+" - Saved")
                self.f = open(self.file,"w")
                self.f.write(self.TextArea.get(1.0,END))
                self.f.close()
            else:
                self.file = None
        else:
            self.master.title(os.path.basename(self.file)+" - Saved")
            self.f = open(self.file,"w")
            self.f.write(self.TextArea.get(1.0,END))
            self.f.close()

    def cutcontent(self):
        self.TextArea.event_generate("<<Cut>>")

    def copycontent(self):
        self.TextArea.event_generate("<<Copy>>")

    def pastecontent(self):
        self.TextArea.event_generate("<<Paste>>")

    def selectall(self,event=None):
        self.TextArea.tag_add(SEL,1.0,END)

    def fontcolor(self):
        self.select_color = colorchooser.askcolor()
        self.TextArea.config(fg=self.select_color[1])

    def about(self):
        ms.showinfo("About","---------------------------------C5---------------------------------\n\nThis Program is completely created by me from python.\nIf you using my code for your project. Don't forget to give credit")

    def manual(self):
        ms.showinfo("Manual","Here we provide you the shortcut-key for easy usage of my Program.\nControl + n: New File\nControl + o: Open File\nControl + s: Save File")

    def exit(self):
        self.close_confirm = ms.askokcancel("Exit","Are you sure to exit")
        if self.close_confirm:
            quit()
        else:
            print("Command Terminated")

    def widget(self):
        # Creating MenuBar
        self.MenuBar = Menu(self.master)
        self.Sub1 = Menu(self.MenuBar,tearoff=0)
        self.Sub2 = Menu(self.MenuBar,tearoff=0)
        self.Sub3 = Menu(self.MenuBar,tearoff=0)
        self.Sub4 = Menu(self.MenuBar,tearoff=0)

        self.Sub1.add_command(label="New",command=self.newFile)
        self.Sub1.add_command(label="Open",command=self.openFile)
        self.Sub1.add_command(label="Save",command=self.saveFile)
        self.MenuBar.add_cascade(label="File",menu=self.Sub1)

        self.Sub2.add_command(label="Cut",command=self.cutcontent)
        self.Sub2.add_command(label="Copy",command=self.copycontent)
        self.Sub2.add_command(label="Paste",command=self.pastecontent)
        self.Sub2.add_separator()
        self.Sub2.add_command(label="Select All",command=self.selectall)
        self.MenuBar.add_cascade(label="Edit",menu=self.Sub2)

        self.Sub3.add_command(label="Font color",command=self.fontcolor)
        self.MenuBar.add_cascade(label="Format",menu=self.Sub3)

        self.Sub4.add_command(label="About",command=self.about)
        self.Sub4.add_command(label="Manual",command=self.manual)
        self.Sub4.add_separator()
        self.Sub4.add_command(label="Exit",command=self.exit)
        self.MenuBar.add_cascade(label="About",menu=self.Sub4)

        self.master.config(menu=self.MenuBar)

        # Main Screen
        self.ScrollBar = Scrollbar(self.master)
        self.ScrollBar.pack(side=RIGHT,fill=Y)
        self.TextArea = Text(self.master,yscrollcommand=self.ScrollBar.set)
        self.ScrollBar.config(command=self.TextArea.yview)
        self.TextArea.pack(fill=BOTH,expand=True)
        self.file = None

        # Shotcut key
        self.master.bind("<Control n>",self.newFile)
        self.master.bind("<Control o>",self.openFile)
        self.master.bind("<Control s>",self.saveFile)
        self.master.bind("<Control a>",self.selectall)

# Creating Tkinter window
tk = Tk()
main(tk)
tk.mainloop()
