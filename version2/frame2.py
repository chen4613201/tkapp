from tkinter import Tk,Button,Canvas,Checkbutton,Entry,\
    Frame,Label,Listbox,Menubutton,Menu,Message,Radiobutton,\
    Scale,Scrollbar,Text,Toplevel,Spinbox,PanedWindow,LabelFrame,ttk,StringVar
from tkinter.ttk import Combobox
from tkinter.constants import *
from version2 import AddrInfoClass
from ping3 import ping
checkNetFrame = Frame()
padxValue = 5
from version2.ServerInfo import ServerInfo



Label(checkNetFrame,text='IPv4地址:').grid(row=0,column=0,padx=padxValue,pady=padxValue)
ipv4Addr = Entry(checkNetFrame)
ipv4Addr.grid(row=0,column=1,padx=padxValue,pady=padxValue)
Message2 = Message(checkNetFrame)
Message2.grid(row=0,column=5,padx=padxValue,pady=padxValue)
message = Message(checkNetFrame)
message.grid(row=1,column=3,columnspan=2)
ServerInfoObj = ServerInfo()
def checkBtn():
    res = ServerInfoObj.NetCheck([ipv4Addr.get()])
    print(ipv4Addr.get())
    Message2.config(text=res[ipv4Addr.get()])

def saveIp():
    ServerInfoObj.addSgSvrInfo(ipv4Addr.get())
    selList.delete(0,'end')
    setListBoxVal()

save = Button(checkNetFrame,text='保存',command=saveIp)
save.grid(row=0,column=2,padx=padxValue,pady=padxValue)
check = Button(checkNetFrame,text='测试连接',command=checkBtn)
check.grid(row=0,column=3,padx=padxValue,pady=padxValue)
Label(checkNetFrame,text='IPv4列表:').grid(row=1,column=0,padx=padxValue,pady=padxValue)
selList = Listbox(checkNetFrame,selectmode=MULTIPLE)
selList.grid(row=1,column=1)

def setListBoxVal():
    SrvList = ServerInfoObj.getServerList()
    for item in SrvList:
        selList.insert('end',item)
setListBoxVal()




def checkBtn2():
    MesList = []
    selListRes = selList.selection_get().split('\n')
    print('----')
    print(selListRes)
    for item in selListRes:
        res = ServerInfoObj.NetCheck([item])
        for k,v in res.items():
            MesList.append(k+v)
    message.config(text=MesList)


check2 = Button(checkNetFrame,text='测试连接',command=checkBtn2)
check2.grid(row=1,column=2)

