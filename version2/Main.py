from tkinter import Tk,Button,Canvas,Checkbutton,Entry,\
    Frame,Label,Listbox,Menubutton,Menu,Message,Radiobutton,\
    Scale,Scrollbar,Text,Toplevel,Spinbox,PanedWindow,LabelFrame,ttk,StringVar
from tkinter.ttk import Combobox
from tkinter.constants import *
from version1 import AddrInfoClass
root = Tk()
root.geometry('450x300')
notebook = ttk.Notebook(root)
from version2.frame1 import confNetInfoFrame
from version2.frame2 import checkNetFrame
notebook.add(confNetInfoFrame,text="IPv4地址信息设置")
notebook.add(checkNetFrame,text="网络ping测试")
notebook.pack(padx=5,pady=5,fill=BOTH,expand=True)
root.mainloop()

