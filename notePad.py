from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newfile():
    global file
    root.title("Untitled-  Notepad")
    file = None
    TextArea.delete(1.0, END)


def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetype=[
                           ("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + "- Notepad")
        TextArea.delete(1.0, END)

        f = open(file, "r")
        TextArea.insert(1.0, f.read())
        f.close()


def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt",
                                 defaultextension=".txt", filetype=[("All Files", "*.*"),
                                                                    ("Text Documents", "*.txt")])

        if file == "":
            file = None

        else:
            # save as a new file
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename((file)+" - Notepad"))

            print("File saved")

    else:
        # save the new file
        f = open(file, "w")
        f.write(TextArea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()


def cut():
    TextArea.event_generate("<<Cut>>")


def copy():
    TextArea.event_generate("<<Copy>>")


def paste():
    TextArea.event_generate("<<Paste>>")


def EditMenu():
    pass


def about():
    showinfo("Notepad", "Notepad by Abhishek")


if __name__ == '__main__':
    #  basic tkinter setup
    root = Tk()
    root.geometry("516x467")
    root.title("Untitled - Notepad")
    root.wm_iconbitmap("MyIco.ico")

    TextArea = Text(root, font="lucida 13")
    TextArea.pack(fill=BOTH, expand=True)

    file = None

    # file menu start
    MenuBar = Menu(root)
    filemenu = Menu(MenuBar, tearoff=0)

    filemenu.add_command(label="New", command=newfile)

    filemenu.add_command(label="Open", command=openFile)

    filemenu.add_command(label="Save", command=saveFile)
    filemenu.add_separator()
    filemenu.add_command(label="exit", command=quitApp)

    MenuBar.add_cascade(label="File", menu=filemenu)

    EditMenu = Menu(MenuBar, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="copy", command=copy)
    EditMenu.add_command(label="paste", command=paste)
    MenuBar.add_cascade(label="Edit", menu=EditMenu)

    HelpMenu = Menu(MenuBar, tearoff=0)
    HelpMenu.add_command(label="About Notepad", command=about)
    MenuBar.add_cascade(label="Help", menu=HelpMenu)

    root.config(menu=MenuBar)

    scrollBar = Scrollbar(TextArea)
    scrollBar.pack(side=RIGHT, fill=Y)
    scrollBar.config(command=TextArea.yview)
    TextArea.config(yscrollcommand=scrollBar.set)

root.mainloop()
