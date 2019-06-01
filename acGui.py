# coding:utf-8
"""
自动操作导出Ex019.4.
"""
import time
import datetime
from pywinauto import application
import pyautogui as pyui
import os
from threading import Thread


class CarsExportClass:
    """
    导出5张Ex
    """

    def __init__(self, sDate, user, pwd, dmsPath, deskPath):
        self.year = str(sDate.year)
        self.month = str(sDate.month)
        self.day = str(int(sDate.day) - 1)
        self.user = user
        self.pwd = pwd
        self.dmsPath = dmsPath
        self.deskPath = deskPath
        self.startApp()

    def startApp(self):
        self.delExFiles()
        app = application.Application(backend="uia").start(self.dmsPath)
        self.app = app
        t = Thread(target=self.monitApp, args=(app,))
        t.setDaemon(True)
        t.start()
        app.window(class_name='TLogin_frm').type_keys(self.pwd)
        app.window(class_name='TLogin_frm').type_keys('{ENTER}')
        time.sleep(10)
        # 判断更新
        try:
            updataApp = app.window(class_name='#32770', title=u'请问')
            updataApp.window(class_name='Button', title=u'确定').click()
            time.sleep(50)
            app.kill()
            self.startApp()
        except Exception as e:
            print('no updata...')
            self.carsUser(app)
            self.carRepair(app)
            self.hous(app)
            self.outbound(app)
            self.carSettle(app)
            time.sleep(5)
            self.status = True
            app.kill()

    def killApp(self):
        self.app.kill()
    def delExFiles(self):
        path = self.deskPath  # ex保存在桌面
        fileList = []
        files = os.listdir(path)
        # print(files)
        for file in files:
            # print(file)
            try:
                if '维修查询20' in file:
                    carRepairExfile = path + file
                    fileList.append(carRepairExfile)
                if '车辆结算明细20' in file:
                    carSettleExfile = path + file
                    fileList.append(carSettleExfile)
                if '出库明细20' in file:
                    carOutboundExfile = path + file
                    fileList.append(carOutboundExfile)
                if '项目查询20' in file:
                    carHousExfile = path + file
                    fileList.append(carHousExfile)
                if '车辆信息20' in file:
                    carsUserExfile = path + file
                    fileList.append(carsUserExfile)
            except Exception as e:
                print(e)
        for delfile in fileList:
            os.remove(delfile)

    def getApp(self, app):
        return app

    def monitApp(self, app):
        """
        监控APP，10分钟后杀死
        :param app:
        :return:
        """
        time.sleep(280)
        app.kill()

    def carsUser(self, app):
        """
        导出客户车辆
        :return:
        """
        cars = app.window(class_name='TMain_frm').window(title_re='客户车辆')
        cars.wrapper_object().click_input()
        time.sleep(5)
        try:
            errorBut = app.window(class_name='#32770', title=u'错误').window(title=u'确定')
            errorBut.click()
            time.sleep(1)
            cars = app.window(class_name='TMain_frm').window(title_re='客户车辆')
            cars.wrapper_object().click_input()
            time.sleep(5)
        except Exception as e:
            pass
        carMange = app.window(class_name='TMain_frm').window(title=u"车辆信息管理")
        carMangeCh = carMange.wrapper_object()
        carMangeCh.children()[0].children()[1].children()[-12].click()
        carMangeCh.children()[0].children()[1].children()[-10].click_input()
        time.sleep(2)
        pyui.press('left')
        pyui.typewrite(self.year, interval=0.25)
        pyui.press('.')
        pyui.typewrite(self.month, interval=0.25)
        pyui.press('.')
        pyui.typewrite(self.day, interval=0.25)
        time.sleep(2)
        carMangeCh.children()[0].children()[1].children()[-11].click_input()
        time.sleep(2)
        pyui.press('left')
        pyui.typewrite(self.year, interval=0.25)
        pyui.press('.')
        pyui.typewrite(self.month, interval=0.25)
        pyui.press('.')
        pyui.typewrite(self.day, interval=0.25)
        time.sleep(2)
        pyui.moveTo(217, 88)
        pyui.click()
        time.sleep(5)
        pyui.moveTo(778, 88)
        pyui.click()
        n = 0
        while True:
            try:
                time.sleep(1)
                enter = app.window(class_name='#32770').children()[0].click()
                break
            except Exception as e:
                pass
                n += 1
                if n > 10:
                    break
                print(e)
        n = 0
        while True:
            try:
                time.sleep(1)
                download = app.window(class_name='Tmsg_tzxx_f').children()[0].click()
                break
            except Exception as e:
                pass
                n += 1
                if n > 10:
                    break
                print(e )
        n = 0
        while True:
            try:
                time.sleep(1)
                enter1 = app.window(class_name='#32770').children()[3].children()[0].click()
                break
            except Exception as e:
                pass
                n += 1
                if n > 10:
                    break
                print(e)

    def carRepair(self, app):
        """
        导出维修查询
        :return:
        """
        cars = app.window(class_name='TMain_frm').window(title_re='维修查询')
        cars.wrapper_object().click_input()
        time.sleep(5)
        try:
            errorBut = app.window(class_name='#32770', title=u'错误').window(title=u'确定')
            errorBut.click()
            time.sleep(1)
            cars = app.window(class_name='TMain_frm').window(title_re='维修查询')
            cars.wrapper_object().click_input()
            time.sleep(5)
        except Exception as e:
            pass
        carMange = app.window(class_name='TMain_frm').window(title=u"工作区")
        carMangeCh = carMange.wrapper_object()
        carMangeCh.children()[0].children()[0].children()[11].click()
        carMangeCh.children()[0].children()[0].children()[8].click()
        carMangeCh.children()[0].children()[0].children()[19].click()
        carMangeCh.children()[0].children()[0].children()[21].click_input()
        pyui.press('left')
        pyui.typewrite(self.year, interval=0.25)
        pyui.press('.')
        pyui.typewrite(self.month, interval=0.25)
        pyui.press('.')
        pyui.typewrite(self.day, interval=0.25)
        time.sleep(2)
        carMangeCh.children()[0].children()[0].children()[20].click_input()
        pyui.press('left')
        pyui.typewrite(self.year, interval=0.25)
        pyui.press('.')
        pyui.typewrite(self.month, interval=0.25)
        pyui.press('.')
        pyui.typewrite(self.day, interval=0.25)
        time.sleep(2)
        pyui.moveTo(216, 88)
        pyui.click()
        time.sleep(4)
        pyui.moveTo(639, 88)
        pyui.click()
        n = 0
        while True:
            try:
                time.sleep(1)
                enter = app.window(class_name='#32770').children()[0].click()
                break
            except Exception as e:
                pass
                n += 1
                if n > 10:
                    break
                print(e)
        n = 0
        while True:
            try:
                time.sleep(1)
                download = app.window(class_name='Tmsg_tzxx_f').children()[0].click()
                break
            except Exception as e:
                pass
                n += 1
                if n > 10:
                    break
                print(e)
        n = 0
        while True:
            try:
                time.sleep(1)
                enter1 = app.window(class_name='#32770').children()[3].children()[0].click()
                break
            except Exception as e:
                pass
                n += 1
                if n > 10:
                    break
                print(e)

    def hous(self, app):
        """
        导出项目查询
        :return:
        """
        cars = app.window(class_name='TMain_frm').window(title_re='项目查询')
        cars.wrapper_object().click_input()
        time.sleep(5)
        try:
            errorBut = app.window(class_name='#32770', title=u'错误').window(title=u'确定')
            errorBut.click()
            time.sleep(1)
            cars = app.window(class_name='TMain_frm').window(title_re='项目查询')
            cars.wrapper_object().click_input()
            time.sleep(5)
        except Exception as e:
            pass
        carMange = app.window(class_name='TMain_frm').window(title=u"工作区")
        carMangeCh = carMange.wrapper_object()
        carMangeCh.children()[0].children()[0].children()[0].children()[1].click_input()
        pyui.press(['down', 'down', 'down'])
        pyui.press(['down', 'down'])
        pyui.press('enter')
        time.sleep(2)
        carMangeCh.children()[0].children()[0].children()[7].click()
        time.sleep(1)
        carMangeCh.children()[0].children()[0].children()[3].click()
        time.sleep(1)
        carMangeCh.children()[0].children()[0].children()[0].click()
        time.sleep(1)
        carMangeCh.children()[0].children()[0].children()[2].click_input()
        pyui.press('left')
        pyui.typewrite(self.year, interval=0.25)
        pyui.press('.')
        pyui.typewrite(self.month, interval=0.25)
        pyui.press('.')
        pyui.typewrite(self.day, interval=0.25)
        time.sleep(2)
        carMangeCh.children()[0].children()[0].children()[1].click_input()
        pyui.press('left')
        pyui.typewrite(self.year, interval=0.25)
        pyui.press('.')
        pyui.typewrite(self.month, interval=0.25)
        pyui.press('.')
        pyui.typewrite(self.day, interval=0.25)
        time.sleep(2)
        pyui.moveTo(220, 88)
        pyui.click()
        time.sleep(3)
        pyui.moveTo(520, 88)
        pyui.click()
        time.sleep(2)
        download = app.window(class_name='Tshuchu_f').wrapper_object()
        n = 0
        while True:
            try:
                time.sleep(1)
                download.children()[3].click()
                break
            except Exception as e:
                pass
                n += 1
                if n > 10:
                    break
                print(e)
        n = 0
        while True:
            try:
                time.sleep(1)
                enter1 = app.window(class_name='#32770').children()[3].children()[0].click()
                break
            except Exception as e:
                pass
                n += 1
                if n > 10:
                    break
                print(e)

    def outbound(self, app):
        """
        导出出库明细
        :return:
        """
        cars = app.window(class_name='TMain_frm').window(title_re='出库查询')
        cars.wrapper_object().click_input()
        time.sleep(5)
        try:
            errorBut = app.window(class_name='#32770', title=u'错误').window(title=u'确定')
            errorBut.click()
            time.sleep(1)
            cars = app.window(class_name='TMain_frm').window(title_re='出库查询')
            cars.wrapper_object().click_input()
            time.sleep(5)
        except Exception as e:
            pass
        carMange = app.window(class_name='TMain_frm').window(title=u"工作区")
        carMangeCh = carMange.wrapper_object()
        carMangeCh.children()[0].children()[1].children()[5].click()
        time.sleep(1)
        carMangeCh.children()[0].children()[1].children()[4].click()
        time.sleep(1)
        carMangeCh.children()[0].children()[1].children()[7].click_input()
        pyui.typewrite(self.month, interval=0.25)
        pyui.press('left')
        pyui.typewrite(self.year, interval=0.25)
        pyui.press('right')
        pyui.press('right')
        pyui.typewrite(self.day, interval=0.25)
        time.sleep(2)
        carMangeCh.children()[0].children()[1].children()[6].click_input()
        pyui.press('left')
        pyui.typewrite(self.year, interval=0.25)
        pyui.press('.')
        pyui.typewrite(self.month, interval=0.25)
        pyui.press('.')
        pyui.typewrite(self.day, interval=0.25)
        time.sleep(2)
        pyui.moveTo(214, 88)
        pyui.click()
        time.sleep(5)
        pyui.moveTo(787, 88)
        pyui.click()
        n = 0
        while True:
            try:
                time.sleep(1)
                enter = app.window(class_name='#32770').children()[0].click()
                break
            except Exception as e:
                pass
                n += 1
                if n > 10:
                    break
                print(e)
        n = 0
        while True:
            try:
                time.sleep(1)
                download = app.window(class_name='Tmsg_tzxx_f').children()[0].click()
                break
            except Exception as e:
                pass
                n += 1
                if n > 10:
                    break
                print(e)
        n = 0
        while True:
            try:
                time.sleep(1)
                enter1 = app.window(class_name='#32770').children()[3].children()[0].click()
                break
            except Exception as e:
                pass
                n += 1
                if n > 10:
                    break
                print(e)

    def carSettle(self, app):
        """
        导出车辆结算明细
        :return:
        """
        cars = app.window(class_name='TMain_frm').window(title_re='车辆结算')
        cars.wrapper_object().click_input()
        time.sleep(5)
        try:
            errorBut = app.window(class_name='#32770', title=u'错误').window(title=u'确定')
            errorBut.click()
            time.sleep(1)
            cars = app.window(class_name='TMain_frm').window(title_re='车辆结算')
            cars.wrapper_object().click_input()
            time.sleep(5)
        except Exception as e:
            pass
        carMange = app.window(class_name='TMain_frm').window(title=u"工作区")
        carMangeCh = carMange.wrapper_object()
        carMangeCh.children()[0].children()[0].children()[3].children()[1].click()
        time.sleep(1)
        carMangeCh.children()[0].children()[0].children()[3].children()[10].click()
        carMangeCh.children()[0].children()[0].children()[3].children()[12].click_input()
        pyui.press('left')
        pyui.typewrite(self.year, interval=0.25)
        pyui.press('.')
        pyui.typewrite(self.month, interval=0.25)
        pyui.press('.')
        pyui.typewrite(self.day, interval=0.25)
        time.sleep(2)
        carMangeCh.children()[0].children()[0].children()[3].children()[11].click_input()
        pyui.press('left')
        pyui.typewrite(self.year, interval=0.25)
        pyui.press('.')
        pyui.typewrite(self.month, interval=0.25)
        pyui.press('.')
        pyui.typewrite(self.day, interval=0.25)
        time.sleep(2)
        carMangeCh.children()[0].children()[0].children()[3].children()[14].click_input()
        pyui.press('down')
        pyui.press('enter')
        time.sleep(1)
        carMangeCh.children()[0].children()[0].children()[3].children()[0].children()[1].click_input()
        pyui.press(['down', 'down', 'down'])
        pyui.press(['down', 'down'])
        pyui.press('enter')
        time.sleep(1)
        pyui.moveTo(213, 90)
        pyui.click()
        time.sleep(4)
        pyui.moveTo(747, 90)
        pyui.click()
        n = 0
        while True:
            try:
                time.sleep(1)
                enter = app.window(class_name='#32770').children()[0].click()
                break
            except Exception as e:
                pass
                n += 1
                if n > 10:
                    break
                print(e)
        n = 0
        while True:
            try:
                time.sleep(1)
                download = app.window(class_name='Tmsg_tzxx_f').children()[0].click()
                break
            except Exception as e:
                pass
                n += 1
                if n > 10:
                    break
                print(e)
        n = 0
        while True:
            try:
                time.sleep(1)
                enter1 = app.window(class_name='#32770').children()[3].children()[0].click()
                break
            except Exception as e:
                pass
                n += 1
                if n > 10:
                    break
                print(e)


if __name__ == "__main__":
    from configparser import ConfigParser

    conf = ConfigParser()
    conf.read(r'conf.ini', encoding='utf-8')
    signCode = conf.get('gboxInfo', 'signCode')
    apiUrl = conf.get('uploadApi', 'url')
    pwd = conf.get('storesInfo', 'pwd')
    user = conf.get('storesInfo', 'user')
    dmsPath = conf.get('storesInfo', 'dmsPath')
    deskPath = conf.get('storesInfo', 'deskPath')
    sDate = datetime.date.today()
    carExport = CarsExportClass(sDate, user=user, pwd=pwd, dmsPath=dmsPath, deskPath=deskPath)
