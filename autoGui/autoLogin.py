#coding:utf-8
from pywinauto import application
import pyautogui as pag
import time

app = application.Application(backend='uia').start('C:\dms\wx\DMSClient.exe')
loginWin = app.window(class_name='TLogin_frm')
pwd = loginWin.wrapper_object().children()[2]
pwd.type_keys('sy3730606@')
pwd.type_keys('{ENTER}')
time.sleep(5)
carList = app.window(class_name='TMain_frm').window(title_re='客户车辆')
carList.wrapper_object().click_input()
time.sleep(5)

# tmp = app.window(class_name='TMain_frm') .window(title='bsSkinToolBar1',class_name='TbsSkinToolBar')
# print(tmp.print_control_identifiers())
pag.click(213,91,duration=1)
time.sleep(3)
pag.click(777,88,duration=1)
time.sleep(3)
alret = app.window(class_name='#32770').window(title='确定')
alret.click()
time.sleep(10)
msg = app.window(class_name='Tmsg_tzxx_f').window(title='下载')
msg.click()
time.sleep(5)
app.kill()