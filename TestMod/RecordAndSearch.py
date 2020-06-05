import tkinter
def RecordAndSearchMain():
    db = pymysql.connect("127.0.0.1","root","12345","XXXXSystem")
    RecordAndSearchUI= Tk()
    RecordAndSearchUI.title('xxxx的综合管理界面')
    RecordAndSearchUI.geometry('1024x768')
    