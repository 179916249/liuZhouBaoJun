# coding:utf-8
"""
获取车主车辆信息
"""
import requests
from logs import LogClass


class CarInfoClass:
    """处理单张车主信息"""
    serverCode = "dataCarImport"  # 服务器代码
    carVIN = ""  # 车辆VIN*
    carLicence = ""  # 车辆牌号*
    carOutColorName = ""  # 车辆颜色(内)
    carInColorName = ""  # 车辆颜色(外)
    carEngineCode = ""  # 车辆动机号
    carSaleInvoiceDate = ""  # 发票日销售日
    carSaleManName = ""  # 销售人员
    carOrderCategoryCode = ""  # 個人訂單
    carOrderDate = ""  # 车辆訂單日期
    carSetCarToCustomDate = ""  # 车辆配車日期
    carOutStockDate = ""  # 车辆交車日期
    carYearFixDate = ""  # 车辆年檢到期
    carLicenceGetDate = ""  # 车辆上牌日
    carInsuranceDate = ""  # 保險到期日
    carInsuranceCompany = ""  # 保險公司
    carInsuranceCode = ""  # 保險公司代号
    carWarrantyDate = ""  # 车辆保修到期
    carPeriodicMaintenanceDate = ""  # 保險到期日
    customPersonName = ""  # 客户名称*
    customPhone = ""  # 客户电话*
    customTelPhone = ""  # 客户家电话
    customCode = ""  # 客户编号
    customLicence = ""  # 客户身份证号
    customBirthday = ""  # 客户生日
    customPhoneArea = ""  # 客户地址区码
    customAddress = ""  # 客户地址
    customMail = ""  # 客户EMail
    customAreaCode = ""  # 客户地址区码
    customWeChat = ""  # 客户微信
    customBaSexID = ""  # 性别ID  女(0),男(1),公司(2),其他(3)
    delivererPersonName = ""  # 使用人名称*
    delivererPhone = ""  # 使用人电话*
    delivererTelPhone = ""  # 使用人家电话
    delivererCode = ""  # 使用人编号
    delivererLicence = ""  # 使用人身份证号
    delivererBirthday = ""  # 使用人生日
    delivererPhoneArea = ""  # 使用人地址区码
    delivererAddress = ""  # 使用人地址
    delivererMail = ""  # 使用人EMail
    delivererAreaCode = ""  # 使用人地址区码
    delivererWeChat = ""  # 使用人微信
    delivererBaSexID = ""  # 性别ID  女(0),男(1),公司(2),其他(3)
    memo = ""  # 备注
    isCommit = ""  # 是否确定提交

    getStatus = False  # 请求状态
    log = LogClass('carinfo.log', 'carinfo')

    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.signCode = kwargs.get('signCode')
        self.apiUrl = kwargs.get('apiUrl')
        self.getCarsUser()

    def getCarsUser(self):
        """
        获取车主列表
        :return:
        """

        self.carVIN = self.kwargs.get("carVIN")
        self.carLicence = self.kwargs.get("carLicence")
        self.carEngineCode = self.kwargs.get("carEngineCode")
        self.carSaleInvoiceDate = self.kwargs.get("carSaleInvoiceDate")
        self.carSaleManName = self.kwargs.get("carSaleManName")
        self.carInsuranceCompany = self.kwargs.get("carInsuranceCompany")
        self.carWarrantyDate = self.kwargs.get("carWarrantyDate")
        self.carPeriodicMaintenanceDate = self.kwargs.get("carPeriodicMaintenanceDate")
        self.customPersonName = self.kwargs.get("customPersonName")
        self.customPhone = self.kwargs.get("customPhone")
        self.customLicence = self.kwargs.get("customLicence")
        self.customAddress = self.kwargs.get("customAddress")
        self.delivererPersonName = self.kwargs.get("delivererPersonName")
        self.delivererAddress = self.kwargs.get("delivererAddress")
        self.delivererBaSexID = self.kwargs.get("delivererBaSexID")
        self.memo = self.kwargs.get("memo")
        self.delivererPhone = self.kwargs.get("delivererPhone")

    def uploadCar(self):
        """
        上传车辆信息
        :return:
        """
        carInfoJson = {
            "serverCode": self.serverCode,
            "signCode": self.signCode,
            "carVIN": self.carVIN,
            "carLicence": self.carLicence,
            "carOutColorName": self.carOutColorName,
            "carInColorName": self.carInColorName,
            "carEngineCode": self.carEngineCode,
            "carSaleInvoiceDate": self.carSaleInvoiceDate,
            "carSaleManName": self.carSaleManName,
            "carOrderCategoryCode": self.carOrderCategoryCode,
            "carOrderDate": self.carOrderDate,
            "carSetCarToCustomDate": self.carSetCarToCustomDate,
            "carOutStockDate": self.carOutStockDate,
            "carYearFixDate": self.carYearFixDate,
            "carLicenceGetDate": self.carLicenceGetDate,
            "carInsuranceDate": self.carInsuranceDate,
            "carInsuranceCompany": self.carInsuranceCompany,
            "carInsuranceCode": self.carInsuranceCode,
            "carWarrantyDate": self.carWarrantyDate,
            "carPeriodicMaintenanceDate": self.carPeriodicMaintenanceDate,
            "customPersonName": self.customPersonName,
            "customPhone": self.customPhone,
            "customTelPhone": self.customTelPhone,
            "customCode": self.customCode,
            "customLicence": self.customLicence,
            "customBirthday": self.customBirthday,
            "customPhoneArea": self.customPhoneArea,
            "customAddress": self.customAddress,
            "customMail": self.customMail,
            "customAreaCode": self.customAreaCode,
            "customWeChat": self.customWeChat,
            "customBaSexID": self.customBaSexID,
            "delivererPersonName": self.delivererPersonName,
            "delivererPhone": self.delivererPhone,
            "delivererTelPhone": self.delivererTelPhone,
            "delivererCode": self.delivererCode,
            "delivererLicence": self.delivererLicence,
            "delivererBirthday": self.delivererBirthday,
            "delivererPhoneArea": self.delivererPhoneArea,
            "delivererAddress": self.delivererAddress,
            "delivererMail": self.delivererMail,
            "delivererAreaCode": self.delivererAreaCode,
            "delivererWeChat": self.delivererWeChat,
            "delivererBaSexID": self.delivererBaSexID,
            "memo": self.memo,
            "isCommit": self.isCommit,
        }
        # print(carInfoJson)
        # """
        
        req = requests.post(self.apiUrl,data=carInfoJson)
        rep = req.json()
        if rep.get('showMsg') == '完成处理':
            self.log.logger.info('{0} updata success...'.format(self.carVIN,))
            print('{0} updata success...'.format(self.carVIN,))
        else:
            self.log.logger.info('{0} updata error...'.format(self.carVIN, ))
            print('{0} updata error...'.format(self.carVIN, ))
        # """
