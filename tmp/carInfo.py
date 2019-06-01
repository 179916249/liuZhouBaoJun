#coding:utf-8
"""处理车主信息"""
from bs4 import BeautifulSoup
from logg import LogClass


class CarInfoClass():
    """处理单张车主信息"""
    carVIN = ""                 #车辆VIN*
    carLicence = ""             #车辆牌号*
    carOutColorName = ""        #车辆颜色(内)
    carInColorName = ""         #车辆颜色(外)
    carEngineCode = ""          #车辆动机号
    carSaleInvoiceDate = ""     #发票日销售日
    carSaleManName = ""         #销售人员
    carOrderCategoryCode = ""   #個人訂單
    carOrderDate = ""           #车辆訂單日期
    carSetCarToCustomDate = ""  #车辆配車日期
    carOutStockDate = ""        #车辆交車日期
    carYearFixDate = ""         #车辆年檢到期
    carLicenceGetDate = ""      #车辆上牌日
    carInsuranceDate = ""       #保險到期日
    carInsuranceCompany = ""    #保險公司
    carInsuranceCode = ""       #保險公司代号
    carWarrantyDate = ""        #车辆保修到期
    carPeriodicMaintenanceDate = ""       #保險到期日
    customPersonName = ""       #客户名称*
    customPhone = ""            #客户电话*
    customTelPhone = ""         #客户家电话
    customCode = ""             #客户编号
    customLicence = ""          #客户身份证号
    customBirthday = ""         #客户生日
    customPhoneArea = ""        #客户地址区码
    customAddress = ""          #客户地址
    customMail = ""             #客户EMail
    customAreaCode = ""         #客户地址区码
    customWeChat = ""           #客户微信
    customBaSexID = ""          #性别ID  女(0),男(1),公司(2),其他(3)
    delivererPersonName = ""    #使用人名称*
    delivererPhone = ""         #使用人电话*
    delivererTelPhone = ""      #使用人家电话
    delivererCode = ""          #使用人编号
    delivererLicence = ""       #使用人身份证号
    delivererBirthday = ""      #使用人生日
    delivererPhoneArea = ""     #使用人地址区码
    delivererAddress = ""       #使用人地址
    delivererMail = ""          #使用人EMail
    delivererAreaCode = ""      #使用人地址区码
    delivererWeChat = ""        #使用人微信
    delivererBaSexID = ""       #性别ID  女(0),男(1),公司(2),其他(3)
    memo = ""                   #备注
    isCommit = ""               #是否确定提交

    getStatus = False           #请求状态
    
    log = LogClass('carinfo.log','carinfo')
    # log.logger.setLevel(logging.ERROR)
    # log.fh.setLevel(logging.ERROR)

    def __init__(self,session,stime,vin,workId,customCarCarLicence,carEngineCode):
        """

        :param session: 登陆认证
        :param stime: 日期
        :param vin: VIN
        :param workId: 工单号
        :param customCarCarLicence: 车辆牌号
        :param carEngineCode: 发动机号
        """
        # super(CarInfoClass,self).__init__('carinfo.log')
        
        self.session = session
        self.stime = stime
        self.vin = vin
        self.workId = workId
        self.start()
        self.customCarCarLicence = customCarCarLicence      #车辆牌号
        self.carEngineCode = carEngineCode                  #发动机号

    def start(self):
        if self.getHtmlInfo():
            return ''
        else:
            return False

    def getHtmlInfo(self):
        try:
            data = {
                "PROG_CODE": "MRP009-1",
                "BILL_NO": self.workId,  # 工单号码
                "FUNC": "U",
                "ENG_NO": self.vin  # VIN
            }
            CarDatas = self.session.post('http://114.80.96.35:8081/uCARE/fdp023_modify.php', data=data)
            html = CarDatas.content.decode('utf8', 'ignore').replace('\r', '').replace('\n', '').replace('\t', '')
            self.carDatas = BeautifulSoup(html, 'lxml')

            td = self.carDatas.findAll(name='td', text='车主代码')[0]  #
            self.customCode = str(td.parent.select('td')[1].select('input')[0].get('value'))  # 车主代号

            data = {
                "FUNC": "Q",
                "HID_CUST_ID": self.customCode  # 车主代码
            }
            carMasterDatas = self.session.post('http://114.80.96.35:8081/uCARE/fdp022_modify.php', data=data)
            html = carMasterDatas.content.decode('utf8', 'ignore').replace('\r', '').replace('\n', '').replace('\t', '')
            self.carMasterDatas = BeautifulSoup(html, 'lxml')
            self.getStatus = True
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 获取车辆牌号失败...'.format(self.stime,self.workId)))
    @property
    def getcarVIN(self):
        """
        车辆VIN*
        :return:
        """
        return self.vin

    @property
    def getcarLicence(self):
        """
        车辆牌号*
        :return:
        """
        return self.customCarCarLicence

    @property
    def getcarOutColorName(self):
        """
        车辆颜色(内)
        :return:
        """
        return ''

    @property
    def getcarInColorName(self):
        """
        车辆颜色(外)
        :return:
        """
        return ''

    @property
    def getcarEngineCode(self):
        """
        车辆动机号
        :return:
        """
        return self.carEngineCode

    @property
    def getcarSaleInvoiceDate(self):
        """
        发票日销售日*
        :return:
        """
        try:
            td = self.carDatas.findAll(name='td', text='领牌日期')[0]  #
            carSaleInvoiceDate = str(td.parent.select('td')[5].select('input')[0].get('value'))  # 发票日销售日
            return carSaleInvoiceDate
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 获取领牌日期失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getcarSaleManName(self):
        """
        销售人员
        :return:
        """
        return ''

    @property
    def getcarOrderCategoryCode(self):
        """
        個人訂單
        :return:
        """
        return ''

    @property
    def getcarOrderDate(self):
        """
        车辆訂單日期
        :return:
        """
        return ''

    @property
    def getcarSetCarToCustomDate(self):
        """
        车辆配車日期
        :return:
        """
        return ''

    @property
    def getcarOutStockDate(self):
        """
        车辆交車日期
        :return:
        """
        return ''

    @property
    def getcarYearFixDate(self):
        """
        车辆年檢到期
        :return:
        """
        return ''

    @property
    def getcarLicenceGetDate(self):
        """
        车辆上牌日
        :return:
        """
        return ''

    @property
    def getcarInsuranceDate(self):
        """
        保險到期日
        :return:
        """
        try:
            td = self.carDatas.findAll(name='td', text='保险到期日')[0]  #
            carInsuranceDate = str(td.parent.select('td')[5].select('input')[0].get('value'))  # 保險到期日
            return carInsuranceDate
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 获取保险到期日失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getcarInsuranceCompany(self):
        """
        保險公司
        :return:
        """
        try:
            td = self.carDatas.findAll(name='td', text='保险公司')[0]  #
            if len(td.parent.select('td')[5].findAll('option[selected=""]')) > 0:
                carInsuranceCompany = str(td.parent.select('td')[5].findAll('option[selected=""]')[0].text)  # 保險公司
            else:
                carInsuranceCompany = ""
            return carInsuranceCompany
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 获取保险公司失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getcarInsuranceCode(self):
        """
        保險公司代号
        :return:
        """
        return ''

    @property
    def getcarWarrantyDate(self):
        """
        车辆保修到期
        :return:
        """
        try:
            td = self.carDatas.findAll(name='td', text='保固迄日')[0]  #
            carWarrantyDate = str(td.parent.select('td')[3].select('input')[0].get('value'))  # 车辆保修到期
            return carWarrantyDate
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 获取车辆保修到期失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getcarPeriodicMaintenanceDate(self):
        """
        车辆定保到期
        :return:
        """
        try:
            td = self.carDatas.findAll(name='td', text='下次定保日期')[0]  #
            carPeriodicMaintenanceDate = str(td.parent.select('td')[3].select('input')[0].get('value'))  # 车辆定保到期
            return carPeriodicMaintenanceDate
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 获取下次定保日期失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getcustomPersonName(self):
        """
        客户名称*
        :return:
        """
        try:
            td = self.carDatas.findAll(name='td', text='车主名称')[0]  #
            self.customPersonName = str(td.parent.select('td')[3].select('input')[0].get('value'))  # 客户名称
            return self.customPersonName
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 获取客户名称失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getcustomPhone(self):
        """
        客户电话*
        :return:
        """
        try:
            td = self.carMasterDatas.findAll(name='td', text='电话(O)')[0]  #
            areaCode = td.parent.select('td')[1].select('input')[0].get('value')
            phoneNumber = td.parent.select('td')[1].select('input')[1].get('value')
            self.customPhone = str(areaCode + ' ' + phoneNumber)  # 客户电话
            if not self.customPhone:
                self.customPhone = self.customTelPhone
            return self.customPhone
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 获取客户电话失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getcustomTelPhone(self):
        """
        客户家电话
        :return:
        """
        try:
            td = self.carMasterDatas.findAll(name='td', text='移动电话一')[0]  #
            self.customTelPhone = str(td.parent.select('td')[1].select('input')[0].get('value'))  # 客户家电话
            return self.customTelPhone
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 获取客户家电话失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getcustomCode(self):
        """
        客户编号
        :return:
        """
        return ''

    @property
    def getcustomLicence(self):
        """
        客户身份证号
        :return:
        """
        try:
            td = self.carMasterDatas.findAll(name='td', text='身分证号／税号')[0]  #
            customLicence = str(td.parent.select('td')[3].select('input')[0].get('value'))  # 客户身份证号
            return customLicence
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 获取客户身份证号失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getcustomBirthday(self):
        """
        客户生日
        :return:
        """
        try:
            td = self.carMasterDatas.findAll(name='td', text='客户生日')[0]  #
            customBirthday = str(td.parent.select('td')[3].select('input')[0].get('value'))  # 客户生日
            return customBirthday
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 获取客户生日失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getcustomPhoneArea(self):
        """
        客户地址区码
        :return:
        """
        return ''

    @property
    def getcustomAddress(self):
        """
        客户地址
        :return:
        """
        try:
            td = self.carMasterDatas.findAll(name='td', text='联络地址')[0]  #
            province = td.parent.select('td')[1].select('select')[0].select('option[selected=""]')[0].text
            city = td.parent.select('td')[1].select('select')[1].select('option[selected=""]')[0].text
            address = td.parent.select('td')[1].select('input[id="TXT05"]')[0].get('value')
            customAddress = str(province + city + address)  # 客户地址
            return customAddress
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 获取客户地址失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getcustomMail(self):
        """
        客户EMail
        :return:
        """
        try:
            td = self.carMasterDatas.findAll(name='td', text='电子信箱')[0]  #
            customMail = str(td.parent.select('td')[1].select('input')[0].get('value'))  # 客户EMail
            return customMail
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 获取客户EMail失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getcustomAreaCode(self):
        """
        客户地址区码
        :return:
        """
        return ''

    @property
    def getcustomWeChat(self):
        """
        客户微信
        :return:
        """
        return ''

    @property
    def getcustomBaSexID(self):
        """
        性别ID  女(0),男(1),公司(2),其他(3)
        :return:
        """
        try:
            td = self.carMasterDatas.findAll(name='td', text='客户别')[0]  #
            customBaSexID = str(td.parent.select('td')[3].select('option[selected=""]')[0].text)  # 性别ID
            if '男' in customBaSexID:
                customBaSexID = "1"
            elif '女' in customBaSexID:
                customBaSexID = "0"
            elif '企业' in customBaSexID:
                customBaSexID = "2"
            else:
                customBaSexID = "3"
            return customBaSexID
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 获取性别ID失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getdelivererPersonName(self):
        """
        使用人名称*
        :return:
        """
        try:
            td = self.carMasterDatas.findAll(name='td', text='联络人')[0]  #
            self.delivererPersonName = str(td.parent.select('td')[1].select('input')[0].get('value'))  # 使用人名称
            if not self.delivererPersonName:
                self.delivererPersonName = self.customPersonName
            return self.delivererPersonName
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 获取客户电话失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getdelivererPhone(self):
        """
        使用人电话*
        :return:
        """
        if not self.delivererPhone:
            self.delivererPhone = self.customTelPhone
        return self.delivererPhone

    @property
    def getdelivererTelPhone(self):
        """
        使用人家电话
        :return:
        """
        return ''

    @property
    def getdelivererCode(self):
        """
        使用人编号
        :return:
        """
        return ''

    @property
    def getdelivererLicence(self):
        """
        使用人身份证号
        :return:
        """
        return ''

    @property
    def getdelivererBirthday(self):
        """
        使用人生日
        :return:
        """
        return ''

    @property
    def getdelivererPhoneArea(self):
        """
        使用人地址区码
        :return:
        """
        return ''

    @property
    def getdelivererAddress(self):
        """
        使用人地址
        :return:
        """
        return ''

    @property
    def getdelivererMail(self):
        """
        使用人EMail
        :return:
        """
        return ''

    @property
    def getdelivererAreaCode(self):
        """
        使用人地址区码
        :return:
        """
        return ''

    @property
    def getdelivererWeChat(self):
        """
        使用人微信
        :return:
        """
        return ''

    @property
    def getdelivererBaSexID(self):
        """
        性别ID  女(0),男(1),公司(2),其他(3)
        :return:
        """
        return ''

    @property
    def getmemo(self):
        """
        备注
        :return:
        """
        try:
            td = self.carMasterDatas.findAll(name='td', text='备注')[0]  #
            memo = str(td.parent.select('td')[1].select('textarea')[0].text)  # 备注
            return memo
        except Exception as e:
            self.log.logger.error((e, '{0} {1} 获取备注失败...'.format(self.stime, self.workId)))
            return ''

    @property
    def getisCommit(self):
        """
        是否确定提交
        :return:
        """
        return ''

