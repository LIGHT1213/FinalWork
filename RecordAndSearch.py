from tkinter import *
from tkinter.ttk import *
import Login
import pymysql
def RecordAndSearchMain():
    RecordAndSearchUI= Tk()
    RecordAndSearchUI.title('xxxx的综合管理界面')
    RecordAndSearchUI.geometry('300x400')
    btn1 = Button(RecordAndSearchUI, text='Record', command=Record)
    btn1.place(x=105, y=78, relwidth=0.3, relheight=0.1)
    btn2 = Button(RecordAndSearchUI, text='Search', command=Search)
    btn2.place(x=105, y=234, relwidth=0.3, relheight=0.1)
    RecordAndSearchUI.mainloop()
def AddCommand():
    db = pymysql.connect("127.0.0.1","root","12345","XXXXSystem")
    mycursor=db.cursor()
    s = "INSERT INTO MoneyRecord VALUES(%s,%s,%s,%s);"
    MoneyDateS = str(MoneyDate.get())
    MoneyNumS = str(MoneyNum.get())
    InOrOutS = str(InOrOut.get())
    if InOrOutS == "收入":
        InOrOutN = 1
    else:
        InOrOutN = 0
    UserName =Login.UserIDSave()
    print("INSERT INTO MoneyRecord VALUES('%s',%s,%s,%s);"%(UserName, InOrOutN, MoneyNumS, MoneyDateS))
    SendRecord = (UserName, InOrOutN, MoneyNumS, MoneyDateS)
    try:
        mycursor.execute(s,SendRecord)
        db.commit()
        print("insert ok!")
        lb1 = Label(RecordUI, text='新增数据成功',font=("黑体",10))
        lb1.place(x=500,y=50, relwidth=0.3, relheight=0.5)
    except:
        print(db.rollback())
        print("insert false!")
        lb1 = Label(RecordUI, text='输入数据不合法',font=("黑体",10))
        lb1.place(x=500,y=50, relwidth=0.3, relheight=0.5)
    lb1 = Label(RecordUI, text='请输入金额',font=("黑体",10))
    lb1.place(x=300,y=200, relwidth=0.1, relheight=0.08)
def Record():
    global RecordUI,InOrOut,MoneyNum,MoneyDate
    db = pymysql.connect("127.0.0.1","root","12345","XXXXSystem")
    RecordUI=Tk()
    RecordUI.title('xxxx的记录界面')
    RecordUI.geometry('824x300')
    var = StringVar()
    InOrOut = Combobox(RecordUI,textvariable=var,values=['收入','支出'])
    InOrOut.place(x=180, y=200,relwidth=0.09)
    MoneyNum = Entry(RecordUI,font=("黑体",10))
    MoneyNum.place(x=400, y=200, relwidth=0.1, relheight=0.08)
    MoneyDate = Entry(RecordUI,font=("黑体",10))
    MoneyDate.place(x=650, y=200, relwidth=0.1, relheight=0.08)
    lb1 = Label(RecordUI, text='请输入金额',font=("黑体",10))
    lb1.place(x=300,y=200, relwidth=0.1, relheight=0.08)
    lb2 = Label(RecordUI, text='请选择收入或支出',font=("黑体",10))
    lb2.place(x=30,y=200, relwidth=0.15, relheight=0.08)
    lb3 = Label(RecordUI, text='请选择日期',font=("黑体",10))
    lb3.place(x=550,y=200, relwidth=0.1, relheight=0.08)
    lb4 = Label(RecordUI, text='例如2020年12月1日则输入20201201',font=("黑体",10))
    lb4.place(x=550, y=250, relwidth=0.4, relheight=0.08)
    btn1 = Button(RecordUI, text='ADD', command=AddCommand)
    btn1.place(x=30, y=100, relwidth=0.1, relheight=0.15)
def Search():
    global UserName
    db = pymysql.connect("127.0.0.1","root","12345","XXXXSystem")
    SearchUI= Tk()
    SearchUI.title('xxxx的查询界面')
    SearchUI.geometry('824x400')
    UserName=Login.UserIDSave()
    s = "SELECT InOrOut,NumOfMoney,InOrOutCauseDate FROM MoneyRecord WHERE SysUserID='%s';"
    print('name=%s'%UserName)
    GetRecord=str(s%UserName)
    cursor = db.cursor()
    cursor.execute(GetRecord)
    txt=Text(SearchUI)
    txt.place(x=0,y=0,relwidth=0.4, relheight=0.4)
    txt.pack()
    t1="           InOrOut           NumOfMoney          InOrOutCauseDate"+'\n'
    txt.insert(END,t1)
    try:
        results = cursor.fetchall()
        for row in results:
            InOrOut = row[0]
            NumOfMoney =row[1]
            InOrOutCauseDate=row[2]
            if (InOrOut==1):
                status='收入'
            else:
                status='支出'
            print("           InOrOut=%s           NumOfMoney=%s          InOrOutCauseDate=%s"%(InOrOut,NumOfMoney,InOrOutCauseDate))
            ResultOfSearch="           %s               %s              %s"
            val=(status,NumOfMoney,InOrOutCauseDate)
            s=str(ResultOfSearch%val)+'\n'
            txt.insert(END,s)
    except:
        print ("没有获取到相关的数据")
        s='没有获取到相关的数据'
        txt.insert(END,s)
    SearchUI.mainloop()

