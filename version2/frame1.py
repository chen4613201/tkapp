from tkinter import Tk,Button,Canvas,Checkbutton,Entry,\
    Frame,Label,Listbox,Menubutton,Menu,Message,Radiobutton,\
    Scale,Scrollbar,Text,Toplevel,Spinbox,PanedWindow,LabelFrame,ttk,StringVar
from tkinter.ttk import Combobox
from tkinter.constants import *
from version2 import AddrInfoClass
confNetInfoFrame = Frame()
padxValue = 5
#标签 用户名密码
Label(confNetInfoFrame,text='地址信息列表:').grid(row=0,column=0,padx=padxValue,pady=20)
Label(confNetInfoFrame,text='IPv4地址:').grid(row=1,column=0,padx=padxValue,pady=padxValue)
Label(confNetInfoFrame,text='子网掩码:').grid(row=2,column=0,padx=padxValue,pady=padxValue)
Label(confNetInfoFrame,text='网关地址:').grid(row=3,column=0,padx=padxValue,pady=padxValue)
Label(confNetInfoFrame,text='首选DNS:').grid(row=4,column=0,padx=padxValue,pady=padxValue)
Label(confNetInfoFrame,text='备选DNS:').grid(row=5,column=0,padx=padxValue,pady=padxValue)
#IPv4地址
ipv4Addr=StringVar()
entry_usr_name=Entry(confNetInfoFrame,textvariable=ipv4Addr)
entry_usr_name.grid(row=1,column=1,padx=padxValue,pady=padxValue)
#子网掩码
netMask=StringVar()
entry_usr_pwd=Entry(confNetInfoFrame,textvariable=netMask)
entry_usr_pwd.grid(row=2,column=1,padx=padxValue,pady=padxValue)
#网关地址
gateWay=StringVar()
entry_usr_pwd=Entry(confNetInfoFrame,textvariable=gateWay)
entry_usr_pwd.grid(row=3,column=1,padx=padxValue,pady=padxValue)
#首选DNS
firstDns=StringVar()
entry_usr_pwd=Entry(confNetInfoFrame,textvariable=firstDns)
entry_usr_pwd.grid(row=4,column=1,padx=padxValue,pady=padxValue)
#备选DNS
secondDns=StringVar()
entry_usr_pwd=Entry(confNetInfoFrame,textvariable=secondDns)
entry_usr_pwd.grid(row=5,column=1,padx=padxValue,pady=padxValue)

combobox = Combobox(confNetInfoFrame,state='readonly')
combobox.grid(row=0,column=1,padx=padxValue,pady=20)

message = Message(confNetInfoFrame)
message.grid(row=1,column=2,rowspan=5,columnspan=3,padx=padxValue,pady=20)

AddrInfoInstance = AddrInfoClass.AddrInfo()
resultSet = AddrInfoInstance.getAllDataFromFile()
combobox['value'] = tuple(resultSet[1])

def set_input_value_by_combobox():
    singleRecord = AddrInfoInstance.getSingleRecord(combobox.get())
    #print(singleRecord)
    ipv4Addr.set(singleRecord[0])
    netMask.set(singleRecord[1])
    gateWay.set(singleRecord[2])
    firstDns.set(singleRecord[3].split('&')[0])
    secondDns.set(singleRecord[3].split('&')[1])

def get_input_value():
    ipv4AddrVal = ipv4Addr.get()
    netMaskVal = netMask.get()
    gateWayVal = gateWay.get()
    firstDnsVal = firstDns.get()
    secondDnsVal = secondDns.get()
    resValue = ipv4AddrVal + ',' + netMaskVal + ',' + gateWayVal + ',' + firstDnsVal + '&' + secondDnsVal
    print(resValue)
    return resValue

def save():
    AddrInfoInstance.modSingleRecord(get_input_value())
    resultSet = AddrInfoInstance.getAllDataFromFile()
    combobox['value'] = tuple(resultSet[1])
    message.config(text='保存成功')
    combobox.current(0)
def set():
    ipv4AddrVal = ipv4Addr.get()
    netMaskVal = netMask.get()
    gateWayVal = gateWay.get()
    firstDnsVal = firstDns.get()
    secondDnsVal = secondDns.get()
    ret_value = AddrInfoInstance.mod_net_info([ipv4AddrVal],[netMaskVal],[gateWayVal],[firstDnsVal],[secondDnsVal])
    message.config(text=ret_value)

def delrecord():
    ret_value = AddrInfoInstance.delSingleRecord(get_input_value())
    resultSet = AddrInfoInstance.getAllDataFromFile()
    combobox['value'] = tuple(resultSet[1])
    message.config(text=ret_value)
    try:
        combobox.current(0)
        set_input_value_by_combobox()
    except Exception as e:
        message.config(text='已没有可用的地址信息')


save_btn = Button(confNetInfoFrame,text='保存',command=save)
save_btn.grid(row=6,column=0)
set_btn = Button(confNetInfoFrame,text='设置',command=set)
set_btn.grid(row=6,column=1)
set_btn = Button(confNetInfoFrame,text='删除',command=delrecord)
set_btn.grid(row=6,column=2)

if len(resultSet[1])>0:
    combobox.current(0)
    set_input_value_by_combobox()

def combobox_select(event):
    set_input_value_by_combobox()

combobox.bind("<<ComboboxSelected>>", combobox_select)
